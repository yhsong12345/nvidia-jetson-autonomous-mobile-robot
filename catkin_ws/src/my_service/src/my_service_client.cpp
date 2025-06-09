#include "ros/ros.h"
#include "my_service/my_service.h"  
#include <cstdlib>   //For atoll()
 
int main(int argc, char **argv)
{
    ros::init(argc, argv, "my_service_client");
    
    if(argc !=3)   //인수값이 부족하면 사용방법 출력
    {
        ROS_INFO("cmd : rosrun my_service my_service_client arg0 arg1");
        ROS_INFO("arg0 : double number, arg1 : double number");
        return 1;    
    }
 
    ros::NodeHandle nh;
 
    ros::ServiceClient client = nh.serviceClient<my_service::my_service>("my_service");
 
    my_service::my_service service;
 
    service.request.a = atoll(argv[1]); // String to Int(long long int)
    service.request.b = atoll(argv[2]);
 
    if(client.call(service)) // Request service 
    {
        ROS_INFO("send service, service.request.a and b : %ld, %ld", (long int)service.request.a, (long int)service.request.b);
        ROS_INFO("receive service, service.response.result : %ld",(long int)service.response.result);    
    }
    else
    {
        ROS_ERROR("Failed to call service");
        return 1;
    }
    return 0;
 
}
