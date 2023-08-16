// Copyright 2016 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "sensor_msgs/msg/imu.hpp"
using std::placeholders::_1;

class MinimalSubscriber : public rclcpp::Node
{
public:
  MinimalSubscriber()
  : Node("minimal_subscriber"), count_(0), latency_(0)
  {
    // subscription_ = this->create_subscription<std_msgs::msg::String>(
    //   "topic", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
    subscription_ = this->create_subscription<sensor_msgs::msg::Imu>(
      "topic", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
  }

private:
  void topic_callback(const sensor_msgs::msg::Imu::SharedPtr msg)
  {
    // RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->header.frame_id.c_str());
    // RCLCPP_INFO(this->get_logger(), "I heard: '%f'", msg->angular_velocity.x);
    // RCLCPP_INFO(this->get_logger(), "I heard: '%d'", msg->header.stamp);
    int64_t t1 = msg->header.stamp.nanosec;
    int64_t t2 = this->now().nanoseconds()%1000000000;
    ((t2-t1)>0) ? latency_ += (t2 - t1)/1000 : latency_ += (t2 - t1)/1000+1000000;
    // latency_ += (t2 - t1)/1000;
    
    // std::cout << "delay : " << (t2 - t1)/1000 << "us" << std::endl;
    count_++;
    if(count_==500) RCLCPP_INFO(this->get_logger(), "avg delay: %ld", latency_/(count_+1));
  }
  rclcpp::Subscription<sensor_msgs::msg::Imu>::SharedPtr subscription_;
  size_t count_;
  int64_t latency_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}
