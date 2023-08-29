#!/bin/bash

data=505
test_type="small"

echo "Launching application, please wait!"
# small payloads
for m in 1 2 5 10
do
    for hz in 100 50 30 10
    do
        for n in 1 2 5 10
        do
            ((wait_time=data/hz+5))
            for payload in 8B 80B 200B 500B 1000B 2000B
            do
                timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=$payload frequency:=$hz n_sub:=${n} m_pub:=${m} &
                timeout $wait_time ./sys_stats $payload $hz $n $m & wait
                python3 data_process.py $hz $n $m $test_type
                sleep 0.5
            done
            python3 cpu_mem_process.py $hz $n $m $test_type
            sleep 0.5
        done
    done
done

test_type="large"
# large payloads
for m in 1 2 5 10
do
    for hz in 100 50 30 10
    do
        for n in 1 2 5 10
        do
            ((wait_time=data/hz+5))
            for payload in 1MB 5MB 10MB 20MB 30MB 50MB
            do
                timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=$payload frequency:=$hz n_sub:=${n} m_pub:=${m} &
                timeout $wait_time ./sys_stats $payload $hz $n $m & wait
                python3 data_process.py $hz $n $m $test_type
                sleep 0.5
            done
            python3 cpu_mem_process.py $hz $n $m $test_type
            sleep 0.5
        done
    done
done

