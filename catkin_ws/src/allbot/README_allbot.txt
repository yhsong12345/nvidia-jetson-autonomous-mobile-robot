######## 2023/03/20 ########
# redefinition launch files 

#-1 run allbot_base only 
$ roslaunch allbot bringup.launch

#-2 allbot_base + lidar only (ydlidar-X4)
$ roslaunch allbot bringup.launch
$ roslaunch allbot lidar_laser.launch 

#-3 allbot_base + lidar + gmapping slam + rviz(w/config)
$ roslaunch allbot bringup.launch
$ roslaunch allbot lidar_slam.launch 
# When finished creating map, run below command with new terminal for saving the map. 
$ rosrun map_server map_saver -f ~/Allbot/allbot/catkin_ws/src/allbot/maps/map

#-4 allbot_base + lidar + navigation + rviz(w/config)
$ roslaunch allbot bringup.launch
$ roslaunch allbot navigate.launch


### add below scripts in "~/.bashrc" and edit it with yours (ex : HOST_IP_ADDR and MASTER_IP_ADDR)  
#
#HOST_IP_ADDR=$(echo "$(hostname -I)" |sed 's/[ ]*$//g')
HOST_IP_ADDR=$(echo "$(hostname -I)" |sed 's/ .*$//g')
#HOST_IP_ADDR="172.30.1.47"
#HOST_IP_ADDR="127.0.0.1" #localhost        # if ROS device's network is not connected, use the localhost IP.   
#MASTER_IP_ADDR=$HOST_IP_ADDR                # If MASTER_IP_ADDR and HOST_IP_ADDR are same, ROS running in stand-alone mode.
MASTER_IP_ADDR="192.168.0.2"
#MASTER_IP_ADDR="172.30.1.46"
export ROS_IP=$HOST_IP_ADDR                 #Target device(ex: Jetson Xavier NX's IP)
export ROS_HOSTNAME=$ROS_IP
export ROS_MASTER_URI=http://$MASTER_IP_ADDR:11311  #Master's IP(ex: Remote(Master) PC that running 'roscore')
export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:~/catkin_make/src
#
#export MBSLIDAR=delta_lidar
#export MBSBASE=mecanum
#
#echo "IP address : [$ROS_IP], Master IP : [$MASTER_IP_ADDR], base : [$MBSBASE], Lidar : [$MBSLIDAR]"
echo "IP address : [$ROS_IP], Master IP : [$MASTER_IP_ADDR]"
#
source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash




