# -----------Install ROS external packages -----------
# ROS Varibles
#rosversion="kinetic" #Ubuntu mate 14.04LTS/16.04LTS
rosversion="melodic" #Ubuntu mate 18.04LTS
#rosversion="noetic"  #Ubuntu mate 20.04LTS
sudo apt-get update
sudo apt-get install -y qt4-dev-tools    qt4-designer
sudo apt-get install -y qt4-doc
sudo apt-get install -y qt4-qtconfig
sudo apt-get install -y qt4-demos
sudo apt-get install -y qt4-designer
sudo apt-get install -y libgeographic-dev
sudo apt-get install -y libv4l-dev 
sudo apt-get install -y build-essential
sudo apt-get install -y chrony
sudo apt-get install -y libbullet-dev 
sudo apt-get install -y libudev-dev
sudo apt-get install -y libusb-dev
sudo apt-get install -y mini-httpd
sudo apt-get install -y ros-$rosversion-roslint
sudo apt-get install -y ros-$rosversion-rosserial
sudo apt-get install -y ros-$rosversion-imu-filter-madgwick
sudo apt-get install -y ros-$rosversion-gmapping
sudo apt-get install -y ros-$rosversion-navigation
sudo apt-get install -y ros-$rosversion-map-server
sudo apt-get install -y ros-$rosversion-rgbd-launch
sudo apt-get install -y ros-$rosversion-costmap-2d
sudo apt-get install -y ros-$rosversion-pcl-ros
sudo apt-get install -y ros-$rosversion-camera-info-manager
sudo apt-get install -y ros-$rosversion-image-transport
sudo apt-get install -y ros-$rosversion-teleop-twist-keyboard 
sudo apt-get install -y ros-$rosversion-robot-upstart
sudo apt-get install -y ros-$rosversion-slam-karto
sudo apt-get install -y ros-$rosversion-geographic-msgs 
sudo apt-get install -y ros-$rosversion-pluginlib
sudo apt-get install -y ros-$rosversion-rosbridge-suite
sudo apt-get install -y ros-$rosversion-robot-pose-publisher
sudo apt-get install -y ros-$rosversion-tf2-web-republisher
sudo apt-get install -y ros-$rosversion-web-video-server
sudo apt-get install -y ros-$rosversion-driver-base 
sudo apt-get install -y ros-$rosversion-driver-libuvc
# install "libuvc", "libgoogle-glog-dev"
sudo apt-get install -y libuvc-dev
sudo apt-get install -y libgoogle-glog-dev
echo "(ALLBOT) ROS External Packages Installed Successfully"