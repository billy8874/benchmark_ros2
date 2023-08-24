import numpy as np
import matplotlib.pyplot as plt


def main():
    xlocs = np.array([1, 2, 3, 4, 5, 6], dtype=np.int32)
    # Load Data 1
    x1 = np.load('small_result/1v10_small_30hz.npy')
    data1 = []
    for i in range(x1.shape[0]):
        data1.append(x1[i,:])
    y1_mean = np.mean(x1, axis=1)
    x1 = xlocs
    # print(np.array(data1)[0])

    plt.hist(np.array(data1)[1]/1000, bins=50)
    plt.xlabel('Latency(ms)')
    plt.ylabel('# of data')
    plt.minorticks_on()
    # plt.grid(which="both")
    # plt.xlim((-100,2100))
    # plt.ylim((0,2000))
    plt.title('Windows Latency Distribution (30Hz)')
    plt.show()   
    

if __name__ == "__main__":
    main()