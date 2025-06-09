#!/usr/bin/env python

import rospy
import actionlib
import cv2
import gtk  # sudo apt update ,  sudo apt install python-gtk2
from actionlib_msgs.msg import GoalStatus, GoalID
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String


scaleX = 1.8
scaleY = 1.8

# Edit goal location as your map
goal_position_1x = 1.3209182024
goal_position_1y = 0.670030355453
goal_position_1w = -0.00143432617188

goal_position_2x = 3.05409431458
goal_position_2y = 6.09153079987
goal_position_2w = 0.00637817382812

goal_position_3x = 1.17408812046
goal_position_3y = 17.0838127136
goal_position_3w = -0.00534057617188


def put_goals_menu():
    cv2.putText(resize, ("1 : R&D Office"), org=(25, 760), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=2)
    cv2.putText(resize, ("2 : Head Office"), org=(25, 790), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=2)
    cv2.putText(resize, ("3 : Front Door"), org=(25, 820), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=2)
    cv2.putText(resize, ("C : Cancel robot navigation"), org=(25, 850), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=2)
    cv2.putText(resize, ("Q : Exit Program"), org=(25, 880), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=2)


def send_goal():
    # set frame
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()

    # set orientation
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal)

    rospy.loginfo('Waiting for the result of send_goal')
    client.wait_for_result()
    
    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Succeeded send_goal')
    else:
        rospy.loginfo('Failed send_goal')


# The movebase_cancel() is same as below commend
# $ rostopic pub -1 /move_base/cancel actionlib_msgs/GoalID -- {}
def movebase_cancel():
    pub = rospy.Publisher('move_base/cancel', GoalID, queue_size=10)
    rate = rospy.Rate(1) 
    goalid = GoalID()
    if not rospy.is_shutdown():
        pub.publish(goalid)
        rate.sleep()


'''
def center_crop(img, set_size):
    h, w, c = img.shape
    if set_size > min(h, w):
        return img
    crop_width = set_size
    crop_height = set_size
    mid_x, mid_y = w//2, h//2
    offset_x, offset_y = crop_width//2, crop_height//2
    crop_img = img[mid_y - offset_y:mid_y + offset_y, mid_x - offset_x:mid_x + offset_x]
    return crop_img
'''


def center_crop_wh(img, set_size_w, set_size_h):
    h, w, c = img.shape
    if set_size_w > min(h, w):
        return img
    crop_width = set_size_w
    crop_height = set_size_h
    mid_x, mid_y = w//2, h//2
    offset_x, offset_y = crop_width//2, crop_height//2
    crop_img = img[mid_y - offset_y:mid_y + offset_y, mid_x - offset_x:mid_x + offset_x]
    return crop_img


#######################################################
#############          Main code          #############
#######################################################

# Get display resolution 
g_width = gtk.gdk.screen_width()
g_height = gtk.gdk.screen_height()
print("Current display resolution : {}x{}".format(g_width, g_height))

# Init send_goal node 
rospy.init_node('send_goal_python')

# Get ActionClient handler on move_base node 
client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

rospy.loginfo('Waiting for the action server to start')
client.wait_for_server()

rospy.loginfo('Action server started, sending the goal')
goal = MoveBaseGoal()

map = cv2.imread("/home/nvidia/catkin_ws/src/allbot/maps/map.pgm")
img = center_crop_wh(map, 800, 600)
#resize = cv2.resize(img, (1280, 1080)) #Adjust for displaying because monitor size 
resize = cv2.resize(img, (1280, 900)) #Adjust for displaying because monitor size 
cv2.putText(resize, ("My map"), org=(25, 25), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255), thickness=2)
put_goals_menu()
cv2.imshow('map',resize)
    
while True:
    ret = cv2.waitKey(0)
    if (ret & 0xFF) == ord('1'):  # R&D Office
        goal.target_pose.pose.position.x = goal_position_1x
        goal.target_pose.pose.position.y = goal_position_1y
        goal.target_pose.pose.orientation.w = goal_position_1w
        send_goal()
    elif (ret & 0xFF) == ord('2'): # Head Office
        goal.target_pose.pose.position.x = goal_position_2x
        goal.target_pose.pose.position.y = goal_position_2y
        goal.target_pose.pose.orientation.w = goal_position_2w
        send_goal()
    elif (ret & 0xFF) == ord('3'): # Front Door
        goal.target_pose.pose.position.x = goal_position_3x
        goal.target_pose.pose.position.y = goal_position_3y
        goal.target_pose.pose.orientation.w = goal_position_3w
        send_goal()
    elif (ret & 0xFF) == ord('c')  or (ret & 0xFF) == ord('C'): # Stop robot moving(navigation)
        rospy.loginfo('Stop robot moving for goal ~~ ')
        movebase_cancel()
    # Add here for more goal location. 
    elif (ret & 0xFF) == ord('q') or (ret & 0xFF) == ord('Q'):
        rospy.loginfo('Closing send_goal application ~~ ')
        cv2.destroyAllWindows()
        #exit()
        break

print("Program finished ~~")
