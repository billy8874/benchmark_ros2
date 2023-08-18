#!/bin/bash

data=505

echo "Launching application, please wait!"
for hz in 1 10 30 50 100
do
    for n in 1 2 5 10
    do
        ((wait_time=data/hz+2))
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=8B frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n small
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=80B frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n small
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=200B frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n small
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=500B frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n small
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=1000B frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n small
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=2000B frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n small
    done
done


data=505

echo "Launching application, please wait!"
for hz in 1 10 30 50 100
do
    for n in 1 2 5 10
    do
        ((wait_time=data/hz+2))
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=1MB frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n large
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=5MB frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n large
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=10MB frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n large
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=20MB frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n large
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=30MB frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n large
        timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=50MB frequency:=$hz n_sub:=${n}
        python3 data_process.py $hz $n large
    done
done
