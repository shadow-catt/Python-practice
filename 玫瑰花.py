# 导入matplotlib库
import matplotlib.pyplot as plt
import numpy as np
# 设置画布大小
plt.figure(figsize=(8, 8))
# 设置极坐标系
ax = plt.subplot(111, projection='polar')
# 设置极坐标的范围和刻度
ax.set_rlim(0, 10)
ax.set_rticks([])
# 生成角度和半径的数据
theta = [i * 0.02 * 3.14 for i in range(1000)]
r = [5 * (1 + np.sin(i * 6)) for i in theta]
# 绘制玫瑰曲线
ax.plot(theta, r, color='red')
# 显示图形
plt.show()
