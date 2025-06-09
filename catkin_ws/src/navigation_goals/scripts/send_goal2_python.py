#!/usr/bin/env python

import rospy
import actionlib
import threading
from actionlib_msgs.msg import GoalStatus, GoalID
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Action status 
# http://docs.ros.org/en/diamondback/api/move_base_msgs/html/msg/MoveBaseAction.html


# Goal location (unit: meter, start from map frame's tf)
# Edit goal location as your map

###################    position_x,   position_y,     position_z  #############
goal_position = [
                    [0.00000000000, 0.00000000000, 0.00000000000000],  #R&D Office
                    [3.92083525658, 6.27109050751, 0.00100612640381],   #Head Office
                    [-10.6301612854, 17.6114349365, 0.000965118408203]   #Front Door 
                ]

######################   x    y    z    w : (x & y must be '0.0')
goal_orientation = [
                        [0.0, 0.0, 0.0, 1.0],
                        [0.0, 0.0, 0.0, 1.0],
                        [0.0, 0.0, 0.0, 1.0],
                        [0.0, 0.0, 0.0, 1.0]
                    ]


#
# Output the goal menu 
#
def ask_goals():    
    print(" ")
    print("1 : R&D Office")
    print("2 : Head Office")
    print("3 : Front Door")
    print("S : Get robot status")
    print("C : Cancel robot navigation")
    print("Q : Exit Program")    
    goal_des = raw_input("Where do you want the robot to go ? ")    # For Python 2
    #goal_des = input("Where do you want the robot to go ? ")       # For Python3
    #print(type(goal_des))
    return goal_des


def wait_result_goal():
    global client
    print(" ")
    rospy.loginfo('---- Waiting for the result of send_goal ----')
    client.wait_for_result()    
    if client.get_state() == GoalStatus.SUCCEEDED:
        print(" ")
        rospy.loginfo('---- Succeeded send_goal ----')
    else:
        print(" ")
        rospy.loginfo('---- Failed send_goal ----')


#
# Send robot to the goal 
#
def send_goal(client, destination):

    goal = MoveBaseGoal()
    # set frame
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()

    # set position where robot to go and the robot's orientation 
    goal.target_pose.pose.position.x = goal_position[destination][0]
    goal.target_pose.pose.position.y = goal_position[destination][1]
    goal.target_pose.pose.position.z = goal_position[destination][2]

    goal.target_pose.pose.orientation.x = goal_orientation[destination][0]
    goal.target_pose.pose.orientation.y = goal_orientation[destination][1]
    goal.target_pose.pose.orientation.z = goal_orientation[destination][2]
    goal.target_pose.pose.orientation.w = goal_orientation[destination][3]

    # Send the robot to goal 
    client.send_goal(goal)

    # Thread for wating robot to goal 
    t = threading.Thread(target=wait_result_goal)
    t.start()


# Cancel the robot moving for navigation
# The movebase_cancel()'s operation is same as below commend
# $ rostopic pub -1 /move_base/cancel actionlib_msgs/GoalID -- {}
def movebase_cancel():
    pub = rospy.Publisher('move_base/cancel', GoalID, queue_size=10)
    rate = rospy.Rate(1) 
    goalid = GoalID()
    if not rospy.is_shutdown():
        pub.publish(goalid)
        rate.sleep()


#
# Main function
#
def main():
    global client

    rospy.init_node('send_goal_python')
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    rospy.loginfo('Waiting for the action server to start')
    client.wait_for_server()

    rospy.loginfo('Action server started, sending the goal')

    while True:
        ret = ask_goals()        
        if ret == "1":  # R&D Office
            send_goal(client, 0)
        elif ret == "2": # Head Office
            send_goal(client, 1)
        elif ret == "3": # Front Door
            send_goal(client, 2)
        elif ret == "s" or ret == "S": # Get robot status
            print("Robot status : ", client.get_state())            
        elif ret == "c" or ret == "C": # Stop robot moving(navigation)
            rospy.loginfo('Stop robot moving for goal ~~ ')
            print("Robot status : ", client.get_state())
            movebase_cancel()
        elif ret == "q" or ret == "Q":
            rospy.loginfo('Closing send_goal application ~~ ')
            break


if __name__ == '__main__':
    main()
    print("Program finished ~~")

