#include "ros/ros.h"
#include "my_service/my_service.h"  

bool calculation(my_service::my_service::Request &request, my_service::my_service::Response &response)
{
    response.result = request.a + request.b;  //Data type are defined at 'my_service.srv'
 
    ROS_INFO("request : x = %ld, y = %ld",(long int)request.a, (long int)request.b);    
    ROS_INFO("sending back response : %ld",(long int)response.result);
 
    return true;    
}               
 
// Main function
int main(int argc, char **argv)
{
    ros::init(argc, argv, "my_service_server");  //Initialize Node Name 'my_service_server'
    ros::NodeHandle nh;  // Get Node handle 
    ros::ServiceServer server = nh.advertiseService("my_service", calculation); //Advertise the service.
    ROS_INFO("ready srv server!!");
 
    ros::spin();   //Process the Callback function until the node terminated.
 
    return 0;
}