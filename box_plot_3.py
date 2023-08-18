import numpy as np
import matplotlib.pyplot as plt


def main():
    # Load Data 1
    x1 = np.load('1v1_small_100hz.npy')
    data1 = []
    for i in range(x1.shape[0]):
        data1.append(x1[i,:])
    y1_mean = np.mean(x1, axis=1)
    x1 = np.array([8, 80, 200, 500, 1000, 2000], dtype=np.int32)

    # Load Data 2
    x2 = np.load('1v5_small_100hz.npy')
    data2 = []
    for i in range(x2.shape[0]):
        data2.append(x2[i,:])
    y2_mean = np.mean(x2, axis=1)
    x2 = np.array([8, 80, 200, 500, 1000, 2000], dtype=np.int32)

    # Load Data 3
    x3 = np.load('1v10_small_100hz.npy')
    data3 = []
    for i in range(x3.shape[0]):
        data3.append(x3[i,:])
    y3_mean = np.mean(x3, axis=1)
    x3 = np.array([8, 80, 200, 500, 1000, 2000], dtype=np.int32)

    # Plot
    fig, ax = plt.subplots()  
    box_wid = 20
    per = (2.5, 97.5)

    # Plot Data 1
    c1='green'
    plt.plot(x1, y1_mean, c1)
    locs, labels = plt.xticks()
    box_pos1 = x1 - np.array([box_wid*1.2], dtype=np.int32)
    bp1 = ax.boxplot(data1, positions=box_pos1 ,showfliers=True, widths=box_wid, whis=per, patch_artist=True,
            boxprops=dict(facecolor=(0,1,0,0.1), color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color='black'))
    
    # Plot Data2
    c2='blue'
    plt.plot(x2, y2_mean, c2)
    box_pos2 = x2
    bp2 = ax.boxplot(data2, positions=box_pos2 ,showfliers=True, widths=box_wid, whis=per, patch_artist=True,
            boxprops=dict(facecolor=(0,0,1,0.1), color=c2),
            capprops=dict(color=c2),
            whiskerprops=dict(color=c2),
            flierprops=dict(color=c2, markeredgecolor=c2),
            medianprops=dict(color='black'))
    
    # Plot Data3
    c3='orange'
    plt.plot(x3, y3_mean, c3)
    box_pos3 = x3 + np.array([box_wid*1.2], dtype=np.int32)
    bp3 = ax.boxplot(data3, positions=box_pos3 ,showfliers=True, widths=box_wid, whis=per, patch_artist=True,
            boxprops=dict(facecolor=(1,0.8,0,0.1), color=c3),
            capprops=dict(color=c3),
            whiskerprops=dict(color=c3),
            flierprops=dict(color=c3, markeredgecolor=c3),
            medianprops=dict(color='black'))
    

    plt.xticks(locs, locs)
    ax.legend([bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0]], ['1v1', '1v5', '1v10'], loc='upper left')
    plt.xlabel('Payload(B)')
    plt.ylabel('Latency(us )')
    plt.xlim((-100,2100))
    plt.ylim((0,3000))
    plt.title('Latency Comparison - # of Subscribers (30Hz)')
    plt.show()   
    

if __name__ == "__main__":
    main()