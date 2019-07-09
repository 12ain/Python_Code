import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
labels = np.array([u'总场次', u'吃鸡数', u'前十数',u'总击杀'])
dataLenth = 4  # 数据长度
data_radar = np.array([60, 1, 15, 13]) # 数据
angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data_radar = np.concatenate((data_radar, [data_radar[0]]))
angles = np.concatenate((angles, [angles[0]]))
plt.polar(angles, data_radar, 'bo-', linewidth=1)
plt.thetagrids(angles * 180/np.pi, labels)
plt.fill(angles, data_radar, facecolor='r', alpha=0.25)
plt.ylim(0, 70)
plt.title('绝地求生战绩')
plt.show()