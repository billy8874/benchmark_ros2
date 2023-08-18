import numpy as np
import matplotlib.pyplot as plt


def main():
    xlocs = np.array([1, 2, 3, 4, 5, 6], dtype=np.int32)
    # Load Data 1
    x1 = np.load('1v10_small_100hz.npy')
    data1 = []
    for i in range(x1.shape[0]):
        data1.append(x1[i,:])
    y1_mean = np.mean(x1, axis=1)
    x1 = xlocs
    # print(np.array(data1)[0])

    plt.hist(np.array(data1)[5], bins=100)
    plt.xlabel('Latency(us)')
    plt.ylabel('# of data')
    plt.minorticks_on()
    plt.grid(which="both")
    # plt.xlim((-100,2100))
    # plt.ylim((0,2000))
    plt.title('Latency Comparison - # of Subscribers (30Hz)')
    plt.show()   
    

if __name__ == "__main__":
    main()