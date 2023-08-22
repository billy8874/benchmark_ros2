#include "rclcpp/logging.hpp"
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "cpp_benchmark/msg/mydata.hpp"

#include <iostream>
#include <fstream>

using std::placeholders::_1;

class MinimalSubscriber : public rclcpp::Node
{
public:
  MinimalSubscriber()
  : Node("minimal_subscriber"), count_(0)
  {
    subscription_ = this->create_subscription<cpp_benchmark::msg::Mydata>(
      "mydata", rclcpp::QoS(10).reliable(), std::bind(&MinimalSubscriber::topic_callback, this, _1));
  }

private:
  void topic_callback(const cpp_benchmark::msg::Mydata::SharedPtr msg)
  {
    // uint64_t t1 = (this->now() - msg->header.stamp).nanoseconds();
    // int64_t t1 = msg->header.stamp.nanosec;
    // int64_t t2 = this->now().nanoseconds() % 1000000000;

    // std::cout << msg->header.frame_id << " time_now: " << msg->header.stamp.sec << " "; 
    // // std::cout << "t1 : " << t1 << ", t2 : " << t2 << std::endl;
    // std::cout << "delay : " << (t2 - t1)/1000 << "us" << std::endl;

    // ((t2-t1)>0) ? latency_ += (t2 - t1)/1000 : latency_ += (t2 - t1)/1000+1000000;
    // ((t2-t1)>0) ? myfile << (t2 - t1)/1000 << ',' : myfile << (t2 - t1)/1000+1000000 << ',';

    count_++;
    if(count_>5 && count_<506) {
      latency_[count_-6][0] = msg->header.stamp.nanosec;
      latency_[count_-6][1] = this->now().nanoseconds();
    }

    if(count_==6) t_start_= this->now().seconds();
    else if(count_==505) {
      RCLCPP_INFO(this->get_logger(), "finish! avg hz: %f", 499/(this->now().seconds()-t_start_));
      // write result to file
      myfile.open(std::string("result/latency/tmp/latency_") + std::string(this->get_name()) + std::string(".csv"));
      for(int i=0; i<500; i++){
        int64_t diff = latency_[i][1] % 1000000000 - latency_[i][0];
        (diff>0) ? myfile << diff/1000 << ',' : myfile << diff/1000+1000000 << ',';
      }
      myfile.close();
    }

    // RCLCPP_INFO(this->get_logger(), "avg delay: %ld", (t2 - t1)/1000);

    // int64_t delay = (t2 - t1)/1000;
    // if(delay>0) std::cout << "delay : " << delay << "us" << std::endl;
    // else std::cout << "delay : " << delay + 1000000 << "us" << std::endl;
  }
  rclcpp::Subscription<cpp_benchmark::msg::Mydata>::SharedPtr subscription_;
  size_t count_;
  int64_t latency_[500][2];
  double t_start_;
  std::ofstream myfile;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}