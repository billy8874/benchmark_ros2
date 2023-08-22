import numpy as np
import matplotlib.pyplot as plt


def main():
    xlocs = np.array([1, 2, 3, 4, 5, 6], dtype=np.int32)
    xlable = np.array(['8B', '80B', '200B', '500B', '1000B', '2000B'], dtype=str)
    # Load Data 1
    x1 = np.load('result/cpu_mem/1v1_small_100hz.npy')

    # Load Data 2
    x2 = np.load('result/cpu_mem/1v10_small_100hz.npy')

    # Plot CPU
    plt.plot(xlocs, x1[:, 0])
    plt.plot(xlocs, x2[:, 0])
    plt.xticks(xlocs, xlable)
    plt.legend(['1v1', '1v10'])
    plt.xlabel('Payload(B)')
    plt.ylabel('CPU Usage(%)')
    # plt.xlim((-100,2100))
    # plt.ylim((0,5000))
    plt.title('CPU Usage - # of Subscribers (100Hz)')
    plt.show() 
    

if __name__ == "__main__":
    main()