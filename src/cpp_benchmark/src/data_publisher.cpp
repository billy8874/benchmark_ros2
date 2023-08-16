#include <chrono>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "cpp_benchmark/msg/mydata.hpp"

using namespace std::chrono_literals;

class MinimalPublisher : public rclcpp::Node
{
public:
  MinimalPublisher()
  : Node("minimal_publisher"), count_(0)
  {
    publisher_ = this->create_publisher<cpp_benchmark::msg::Mydata>("mydata", rclcpp::QoS(10).reliable());
    timer_ = this->create_wall_timer(
      200ms, std::bind(&MinimalPublisher::timer_callback, this));
    this->declare_parameter("fliename", rclcpp::PARAMETER_STRING);
  }
  
  MinimalPublisher(char * argv[])
  : Node("minimal_publisher"), count_(0)
  {
    publisher_ = this->create_publisher<cpp_benchmark::msg::Mydata>("mydata", rclcpp::QoS(10).reliable());
    unsigned long long us = 1000000/std::stod(argv[2]);
    auto dt = std::chrono::microseconds(us);
    timer_ = this->create_wall_timer(
      dt, std::bind(&MinimalPublisher::timer_callback, this));
    
    // Convert String to Byte Size
    size_t valueEnd = std::string(argv[1]).find_first_not_of("0123456789");
    std::string valueStr = std::string(argv[1]).substr(0, valueEnd);
    size_t value = stoi(valueStr);
    std::string unit = std::string(argv[1]).substr(valueEnd);
    size_t bytes;
    if (unit == "KB" || unit == "kb") {
        bytes = value * 1000;
    } else if (unit == "MB" || unit == "mb") {
        bytes = value * 1000 * 1000;
    } else {
        bytes = value;
    }

    msg_.data.resize(bytes);
  }

private:
  void timer_callback()
  {
    msg_.header.stamp = this->now();
    msg_.header.frame_id = "frame000";
    count_++;
    // RCLCPP_INFO(this->get_logger(), "Image %ld published:", count_++);
    publisher_->publish(msg_); 
  }
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<cpp_benchmark::msg::Mydata>::SharedPtr publisher_;
  size_t count_;
  cpp_benchmark::msg::Mydata msg_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>(argv));
  rclcpp::shutdown();
  return 0;
}