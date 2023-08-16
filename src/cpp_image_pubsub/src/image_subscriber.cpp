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

#include "cv_bridge/cv_bridge.h"
#include "image_transport/image_transport.hpp"
#include "opencv2/highgui.hpp"
#include "rclcpp/logging.hpp"
#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/image.hpp"
#include <iostream>
#include <fstream>

// void imageCallback(const sensor_msgs::msg::Image::ConstSharedPtr & msg)
// {
//   try {
//     cv::imshow("view", cv_bridge::toCvShare(msg, "bgr8")->image);
//     cv::waitKey(10);
//   } catch (const cv_bridge::Exception & e) {
//     auto logger = rclcpp::get_logger("my_subscriber");
//     RCLCPP_ERROR(logger, "Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
//   }
// }

// int main(int argc, char ** argv)
// {
//   rclcpp::init(argc, argv);
//   rclcpp::NodeOptions options;
//   rclcpp::Node::SharedPtr node = rclcpp::Node::make_shared("image_listener", options);
//   cv::namedWindow("view");
//   cv::startWindowThread();
//   image_transport::ImageTransport it(node);
//   image_transport::Subscriber sub = it.subscribe("camera/image", 1, imageCallback);
//   rclcpp::spin(node);
//   cv::destroyWindow("view");

//   return 0;
// }

using std::placeholders::_1;

class MinimalSubscriber : public rclcpp::Node
{
public:
  MinimalSubscriber()
  : Node("minimal_subscriber"), count_(0)
  {
    subscription_ = this->create_subscription<sensor_msgs::msg::Image>(
      "camera/image", rclcpp::QoS(10).reliable(), std::bind(&MinimalSubscriber::topic_callback, this, _1));
    // char c2[100];
    // strcpy(c2,this->get_name());
    myfile.open(std::string("latency_") + std::string(this->get_name()) + std::string(".csv"));
  }

private:
  void topic_callback(const sensor_msgs::msg::Image::SharedPtr msg)
  {
    try {
      // cv::imshow("view", cv_bridge::toCvShare(msg, "bgr8")->image);
      // cv::waitKey(10);

      // uint64_t t1 = (this->now() - msg->header.stamp).nanoseconds();
      int64_t t1 = msg->header.stamp.nanosec;
      int64_t t2 = this->now().nanoseconds() % 1000000000;

      // std::cout << msg->header.frame_id << " time_now: " << msg->header.stamp.sec << " "; 
      // // std::cout << "t1 : " << t1 << ", t2 : " << t2 << std::endl;
      // std::cout << "delay : " << (t2 - t1)/1000 << "us" << std::endl;

      // ((t2-t1)>0) ? latency_ += (t2 - t1)/1000 : latency_ += (t2 - t1)/1000+1000000;
      ((t2-t1)>0) ? myfile << (t2 - t1)/1000 << ',' : myfile << (t2 - t1)/1000+1000000 << ',';

      count_++;
      if(count_==1) t_start_= this->now().seconds();
      else if(count_==500) {
        RCLCPP_INFO(this->get_logger(), "finish! avg hz: %f", (count_-1)/(this->now().seconds()-t_start_));
        myfile.close();
      }

      // RCLCPP_INFO(this->get_logger(), "avg delay: %ld", (t2 - t1)/1000);

      // int64_t delay = (t2 - t1)/1000;
      // if(delay>0) std::cout << "delay : " << delay << "us" << std::endl;
      // else std::cout << "delay : " << delay + 1000000 << "us" << std::endl;

    } catch (const cv_bridge::Exception & e) {
      auto logger = rclcpp::get_logger("my_subscriber");
      RCLCPP_ERROR(logger, "Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
    }
  }
  rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr subscription_;
  size_t count_;
  int64_t latency_[500];
  double t_start_;
  std::ofstream myfile;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  // cv::namedWindow("view");
  // cv::startWindowThread();
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  // cv::destroyWindow("view");
  rclcpp::shutdown();
  return 0;
}