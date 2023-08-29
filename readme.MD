# ROS2 Benchmark; [![ROS noetic](https://img.shields.io/badge/ROS2-Humble-blue)](https://docs.ros.org/en/humble/index.html)

This is a ROS2 package using with minimal publisher and subscriber to benchmarking and comparing the performance between different middlewares.

This package includes two parts:

* **ROS2 package:** Follow tutorials on the website to create publishers and subscribers as well as launch file to benchmark.
* **Cpp Linux System Stats:** Use a github repo to help us get system status including CPU and Memory usage. [cpp-linux-system-stats](https://github.com/improvess/cpp-linux-system-stats)

## Building and Complie

Go to the root folder of the workspace using `colcon build` to build ROS2 packages.
```
colcoun build
```

Also, compile the system status cpp to get system information.
```
./compile_sys_stats_cpp.sh
```


## Launch and Execute
After building all necessary packages, run the following command to start a benchmark.
```
./benchmark.sh
```
You can modify m, n, hz, payload in benchmark.sh file to run specific combinations of the benchmark.
