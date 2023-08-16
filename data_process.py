import numpy as np
import csv
import matplotlib.pyplot as plt
import sys

def main():
    fre = sys.argv[1]
    sub_num = sys.argv[2]
    size = sys.argv[3]

    np_data = np.zeros((int(sub_num),500),dtype=np.double)

    for i in range(int(sub_num)):
        filename = 'latency_subscriber_'+str(i)+'.csv'
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        data[0].pop()
        np_data[i] = np.array(data, dtype=np.double)

    data_max = np.max(np_data, axis=0)
    mean_latency = np.mean(data_max)
    # print(data_max)
    print("Mean Latency: ", mean_latency)
    filename = '1v'+sub_num+'_'+size+'_'+fre+'hz'
    try:
        x = np.load(filename+'.npy')
        x = np.vstack((x, data_max[None,:]))
        np.save(filename,x)
    except:
        x = data_max[None,:]
        np.save(filename,x)
    
    

if __name__ == "__main__":
    main()