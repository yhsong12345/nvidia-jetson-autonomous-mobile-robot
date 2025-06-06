#include "allbot_pid/allbot_pid_core.h"

AllbotPID::AllbotPID()
{
}

AllbotPID::~AllbotPID()
{
}

void AllbotPID::publishMessage(ros::Publisher *pub_message)
{
  allbot_msgs::PID msg;
  msg.p = p_;
  msg.d = d_;
  msg.i = i_;
  pub_message->publish(msg);
}

void AllbotPID::messageCallback(const allbot_msgs::PID::ConstPtr &msg)
{
  p_ = msg->p;
  d_ = msg->d;
  i_ = msg->i;

  //echo P,I,D
  ROS_INFO("P: %f", p_);
  ROS_INFO("D: %f", d_);
  ROS_INFO("I: %f", i_);
}

void AllbotPID::configCallback(allbot_pid::allbotPIDConfig &config, double level)
{
  //for PID GUI
  p_ = config.p;
  d_ = config.d;
  i_ = config.i;

}
