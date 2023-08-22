#!/bin/bash

data=505
test_type="small"

echo "Launching application, please wait!"

if [[ "$test_type" == "small" ]]; then
    # small payloads
    for m in 1 #2 5 10
    do
        for hz in 100
        do
            for n in 1 2 5 10
            do
                ((wait_time=data/hz+2))
                for payload in 8B 80B 200B 500B 1000B 2000B
                do
                    timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=$payload frequency:=$hz n_sub:=${n} m_pub:=${m}
                    python3 data_process.py $hz $n $m $test_type
                done
            done
        done
    done
else
    # large payloads
    for m in 1 2 5 10
    do
        for hz in 1 10 30 50 100
        do
            for n in 1 2 5 10
            do
                ((wait_time=data/hz+2))
                for payload in 1MB 5MB 10MB 20MB 30MB 50MB
                do
                    timeout $wait_time ros2 launch cpp_benchmark broadcast.launch.py payload_size:=1MB frequency:=$hz n_sub:=${n} m_pub:=${m}
                    python3 data_process.py $hz $n $m $test_type
                done
            done
        done
    done
fi

