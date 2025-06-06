#ifndef SR_ALLBOT_PID_CORE_H
#define SR_ALLBOT_PID_CORE_H

#include "ros/ros.h"
#include "ros/time.h"

// Custom message includes. Auto-generated from msg/ directory.
#include "allbot_msgs/PID.h"

// Dynamic reconfigure includes.
#include <dynamic_reconfigure/server.h>
// Auto-generated from cfg/ directory.
#include <allbot_pid/allbotPIDConfig.h>

class AllbotPID
{
public:
  AllbotPID();
  ~AllbotPID();
  void configCallback(allbot_pid::allbotPIDConfig &config, double level);
  void publishMessage(ros::Publisher *pub_message);
  void messageCallback(const allbot_msgs::PID::ConstPtr &msg);

  double p_;
  double d_;
  double i_;

};
#endif
