# 认识

## 1.1 Figure （类似画板）
- 在进行任何绘图前，都需要一个Figure对象，可以理解成我们需要一张画板才能开始绘图
```python
import matplotlib.pylot as plt
fig = plt.figure()
```

## 1.2 Axes
```python
ax = fig.add_subplot(111) # 将面板划分为1*1方格，在第一个位置生成axes；可传入数组，效果一样
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
       ylabel='Y-Axis', xlabel='X-Axis') # 设置轴的参数
```

## 1.3 Mult Axes
```python
fig, axes = plt.subplots(2, 2) # 划分为2行2列，共4个axes对象
axes[0,0].set(title='Upper Left')
axes[0,1].set(title='Upper Right')
axes[1,0].set(title='Lower Left')
axes[1,1].set(title='Lower Right')
```