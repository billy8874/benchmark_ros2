// Copyright 2021, Open Source Robotics Foundation, Inc.
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

// #include "cv_bridge/cv_bridge.h"
// #include "image_transport/image_transport.hpp"
// #include "opencv2/core/mat.hpp"
// #include "opencv2/imgcodecs.hpp"
// #include "rclcpp/rclcpp.hpp"

// int main(int argc, char ** argv)
// {
//   rclcpp::init(argc, argv);
//   rclcpp::NodeOptions options;
//   rclcpp::Node::SharedPtr node = rclcpp::Node::make_shared("image_publisher", options);
//   image_transport::ImageTransport it(node);
//   image_transport::Publisher pub = it.advertise("camera/image", 1);

//   cv::Mat image = cv::imread(argv[1], cv::IMREAD_COLOR);
//   std_msgs::msg::Header hdr;
//   sensor_msgs::msg::Image::SharedPtr msg = cv_bridge::CvImage(hdr, "bgr8", image).toImageMsg();

//   rclcpp::WallRate loop_rate(5);
//   int count_=0;
//   while (rclcpp::ok()) {
//     pub.publish(msg);
//     // RCLCPP_INFO(node->get_logger(), "Publishing: '%d'", count_++);
//     rclcpp::spin_some(node);
//     loop_rate.sleep();
//   }
// }

#include <chrono>
#include <memory>

#include "cv_bridge/cv_bridge.h"
// #include "image_transport/image_transport.hpp"
#include "opencv2/core/mat.hpp"
#include "opencv2/imgcodecs.hpp"
#include "rclcpp/rclcpp.hpp"

#include "std_msgs/msg/string.hpp"
#include "sensor_msgs/msg/imu.hpp"

using namespace std::chrono_literals;

class MinimalPublisher : public rclcpp::Node
{
public:
  MinimalPublisher()
  : Node("minimal_publisher"), count_(0)
  {
    publisher_ = this->create_publisher<sensor_msgs::msg::Image>("camera/image", rclcpp::QoS(10).reliable());
    timer_ = this->create_wall_timer(
      200ms, std::bind(&MinimalPublisher::timer_callback, this));
    this->declare_parameter("fliename", rclcpp::PARAMETER_STRING);
  }
  
  MinimalPublisher(char * argv[])
  : Node("minimal_publisher"), count_(0)
  {
    publisher_ = this->create_publisher<sensor_msgs::msg::Image>("camera/image", rclcpp::QoS(10).reliable());
    unsigned long long us = 1000000/std::stod(argv[2]);
    auto dt = std::chrono::microseconds(us);
    timer_ = this->create_wall_timer(
      dt, std::bind(&MinimalPublisher::timer_callback, this));
    image = cv::imread(argv[1], cv::IMREAD_COLOR);
    msg_ = *cv_bridge::CvImage(std_msgs::msg::Header(), "bgr8", image).toImageMsg();
  }

private:
  void timer_callback()
  {
    //// monkey stream video example
    // std::stringstream ss;
    // ss << std::setw(3) << std::setfill('0') << count_%577+1;
    // std::string s = ss.str();
    // std::string file_name = "/root/ros2_ws/imgs/monkey/monkey5_" + s + ".jpg";
    // std::cout << file_name << std::endl;
    msg_.header.stamp = this->now();
    msg_.header.frame_id = "frame ID: " + std::to_string(count_++);
    // RCLCPP_INFO(this->get_logger(), "Image %ld published:", count_++);
    publisher_->publish(msg_); 
  }
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<sensor_msgs::msg::Image>::SharedPtr publisher_;
  size_t count_;
  cv::Mat image;
  sensor_msgs::msg::Image msg_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>(argv));
  rclcpp::shutdown();
  return 0;
}