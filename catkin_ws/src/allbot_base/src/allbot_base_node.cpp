#include <ros/ros.h>
#include "allbot_base/allbot_base.h"

int main(int argc, char** argv )
{
    ros::init(argc, argv, "allbot_base_node");
    AllbotBase allbot;
    ros::spin();
    return 0;
}
