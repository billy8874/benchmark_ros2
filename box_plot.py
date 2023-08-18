import numpy as np
import matplotlib.pyplot as plt


def main():
    xlocs = np.array([1, 2, 3, 4, 5, 6], dtype=np.int32)
    # Load Data 1
    x1 = np.load('1v1_small_10hz.npy')
    data1 = []
    for i in range(x1.shape[0]):
        data1.append(x1[i,:])
    y1_mean = np.mean(x1, axis=1)
    x1 = xlocs

    # Load Data 2
    x2 = np.load('1v5_small_10hz.npy')
    data2 = []
    for i in range(x2.shape[0]):
        data2.append(x2[i,:])
    y2_mean = np.mean(x2, axis=1)
    x2 = xlocs

    # Plot
    fig, ax = plt.subplots()
    per = (2.5, 97.5)
    per = 3.5
    box_wid = 0.1
    # Plot Data 1
    c1='green'
    plt.plot(x1, y1_mean, c1)
    locs, labels = plt.xticks()
    box_pos1 = x1 - np.array([box_wid/2*1.2], dtype=np.float64)
    bp1 = ax.boxplot(data1, positions=box_pos1 ,showfliers=True, widths=box_wid, whis=per, patch_artist=True,
            boxprops=dict(facecolor=(0,1,0,0.1), color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color='black'))
    
    # Plot Data2
    c2='blue'
    plt.plot(x2, y2_mean, c2)
    box_pos2 = x2 + np.array([box_wid/2*1.2], dtype=np.float64)
    bp2 = ax.boxplot(data2, positions=box_pos2 ,showfliers=True, widths=box_wid, whis=per, patch_artist=True,
            boxprops=dict(facecolor=(0,0,1,0.1), color=c2),
            capprops=dict(color=c2),
            whiskerprops=dict(color=c2),
            flierprops=dict(color=c2, markeredgecolor=c2),
            medianprops=dict(color='black'))
    

    plt.xticks(locs, locs)
    ax.legend([bp1["boxes"][0], bp2["boxes"][0]], ['1v1', '1v10'], loc='upper left')
    plt.xlabel('Payload(B)')
    plt.ylabel('Latency(us )')
    # plt.xlim((-100,2100))
    plt.ylim((0,2000))
    plt.title('Latency Comparison - # of Subscribers (30Hz)')
    plt.show()   
    

if __name__ == "__main__":
    main()