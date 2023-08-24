import numpy as np
import matplotlib.pyplot as plt


def main():
    per_lat = (100 - 95) * 5
    xlocs = np.array([1, 2, 3, 4, 5, 6], dtype=np.int32)
    xlable = np.array(['8B', '80B', '200B', '500B', '1000B', '2000B'], dtype=str)
    # xlable = np.array(['1MB', '5MB', '10MB', '20MB', '30MB', '50MB'], dtype=str)
    # Load Data 1
    x1 = np.load('result/latency/1v5_x5_small_100hz.npy')
    data1 = []
    for i in range(x1.shape[0]):
        data1.append(np.sort(x1[i,:])[:-per_lat]/1000)
    y1_mean = np.mean(np.array(data1), axis=1)
    x1 = xlocs

    # Load Data 2
    x2 = np.load('result/latency/1v5_x7_small_100hz.npy')
    data2 = []
    for i in range(x2.shape[0]):
        data2.append(np.sort(x2[i,:])[:-per_lat]/1000)
    y2_mean = np.mean(np.array(data2), axis=1)
    x2 = xlocs

    # Plot
    fig, ax = plt.subplots()
    per = (0.5, 99.5)
    box_wid = 0.2
    # Plot Data 1
    c1='green'
    plt.plot(x1, y1_mean, c1)
    box_pos1 = x1 - np.array([box_wid/2*1.2], dtype=np.float64)
    bp1 = ax.boxplot(data1, positions=box_pos1 ,showfliers=True, widths=box_wid, whis=per, patch_artist=True,
            boxprops=dict(facecolor=[0, 1, 0, 0.2], color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color='black'))
    # q1 = np.percentile(data1, 25, axis=1)
    # q2 = np.percentile(data1, 50, axis=1)
    # q3 = np.percentile(data1, 75, axis=1)
    # perc = per * (q3 - q1)
    # print((data1[0][data1[0] > (q3 + perc)[0]]).shape[0], (data1[0][data1[0] < (q1 - perc)[0]]).shape[0])
    
    # Plot Data2
    c2='blue'
    plt.plot(x2, y2_mean, c2)
    box_pos2 = x2 + np.array([box_wid/2*1.2], dtype=np.float64)
    bp2 = ax.boxplot(data2, positions=box_pos2 ,showfliers=True, widths=box_wid, whis=per, patch_artist=True,
            boxprops=dict(facecolor=[0, 0, 1, 0.2], color=c2),
            capprops=dict(color=c2),
            whiskerprops=dict(color=c2),
            flierprops=dict(color=c2, markeredgecolor=c2),
            medianprops=dict(color='black'))
    

    plt.xticks(xlocs, xlable)
    ax.legend([bp1["boxes"][0], bp2["boxes"][0]], ['1v1', '1v10'], loc='upper left')
    plt.xlabel('Payload(B)')
    plt.ylabel('Latency(ms)')
    # plt.xlim((-100,2100))
    # plt.ylim((0,5))
    plt.title('ROS2 on Linux Docker (30Hz)')
    plt.show()   
    

if __name__ == "__main__":
    main()