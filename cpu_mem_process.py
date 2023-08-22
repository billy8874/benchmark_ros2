import numpy as np
import csv
import sys

def main():
    fre = sys.argv[1]
    sub_num = sys.argv[2]
    pub_num = sys.argv[3]
    size = sys.argv[4]

    usage = np.zeros((6, 2),dtype=np.double)
    payloads = []

    if size=='large': 
        payloads = ['1MB', '5MB', '10MB', '20MB', '30MB', '50MB']
    elif size=='small':
        payloads = ['8B', '80B', '200B', '500B', '1000B', '2000B']
    
    for payload, i in zip(payloads, range(len(payloads))):
        filename = 'result/cpu_mem/tmp/1v'+sub_num+'_'+payload+'_'+fre+'hz.csv'
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        usage[i] = np.mean(np.array(data, dtype=float), axis=0)
        # data[0].pop()
        # np_data[i] = np.array(data, dtype=np.double)

    print("CPU and Memory Usage: ", usage)
    # Save to .npy file
    filename = 'result/cpu_mem/1v'+sub_num+'_x'+pub_num+'_'+size+'_'+fre+'hz'
    np.save(filename,usage)
    
if __name__ == "__main__":
    main()