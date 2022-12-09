# Matplotlib入门[06]——figures，subplots，axes和ticks对象

> 参考：
>
> + [https://ailearning.apachecn.org/](https://ailearning.apachecn.org/)
> + [Matplotlib官网](https://matplotlib.org/)
> + [matplotlib xticks yticks](https://blog.csdn.net/claroja/article/details/77451537)
>
> 
>
> 使用Jupyter进行练习



![Logo image](https://matplotlib.org/stable/_static/images/logo2.svg)



```python
import matplotlib.pyplot as plt
```

## figures,axes和ticks的关系

这些对象的关系可以用下图表示：
![图1](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/artists_figure.png)

具体结构：
![图2](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/artists_tree.png)

## figure对象

`figure` 对象是最外层的绘图单位，默认是以 `1` 开始编号（**MATLAB** 风格，`Figure 1, Figure 2, ...`），可以用 `plt.figure()` 产生一幅图像，除了默认参数外，可以指定的参数有：

- `num` - 编号
- `figsize` - 图像大小
- `dpi` - 分辨率
- `facecolor` - 背景色
- `edgecolor` - 边界颜色
- `frameon` - 边框

这些属性也可以通过 `Figure` 对象的 `set_xxx` 方法来改变。


```python
fig = plt.figure(num=1,figsize=(4,2),frameon=True)
fig.set_facecolor('pink')
plt.plot([1,2,3,4])
plt.show()
```


![06figures,subplots,axes和ticks对象_7_0](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/06figures,subplots,axes%E5%92%8Cticks%E5%AF%B9%E8%B1%A1_7_0.png)
    


## ticks对象

ticks 用来注释轴的内容，我们可以通过控制它的属性来决定在哪里显示轴、轴的内容是什么等等。

```python
xticks()返回了两个对象,一个是刻标(locs)，另一个是刻度标签
locs, labels = xticks()

# 显示x轴的刻标
xticks( arange(6) )

# 显示x轴的刻标以及对应的标签
xticks( arange(5), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue') )
```

此外xticks()还可以传入matplotlib.text.Text类的属性来控制显示的样式

```python
xticks( arange(12), calendar.month_name[1:13], rotation=17 )
```

如果不想显示ticks则可以可以传入空的参数如`yticks([])`


```python
import numpy as np
import calendar
plt.plot([0,1,2,3])
plt.xticks( np.arange(5), ('Mon','Tue','Wed','Thur','Fri'), rotation=17 )
plt.show()
```


![06figures,subplots,axes和ticks对象_12_0](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/06figures,subplots,axes%E5%92%8Cticks%E5%AF%B9%E8%B1%A1_12_0.png)
    


## subplot和axes对象

### subplot对象

`subplot` 主要是使用网格排列子图：


```python
plt.subplot(2,1,1)
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'subplot(2,1,1)',ha='center',va='center',size=24,alpha=.5)

plt.subplot(2,1,2)
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'subplot(2,1,2)',ha='center',va='center',size=24,alpha=.5)

plt.show()
```


![06figures,subplots,axes和ticks对象_16_0](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/06figures,subplots,axes%E5%92%8Cticks%E5%AF%B9%E8%B1%A1_16_0.png)
    


更高级的可以用`gridspec`绘图：


```python
import matplotlib.gridspec as gridspec

G = gridspec.GridSpec(3, 3)

axes_1 = plt.subplot(G[0, :])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 1',ha='center',va='center',size=24,alpha=.5)

axes_2 = plt.subplot(G[1,:-1])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 2',ha='center',va='center',size=24,alpha=.5)

axes_3 = plt.subplot(G[1:, -1])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 3',ha='center',va='center',size=24,alpha=.5)

axes_4 = plt.subplot(G[-1,0])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 4',ha='center',va='center',size=24,alpha=.5)

axes_5 = plt.subplot(G[-1,-2])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'Axes 5',ha='center',va='center',size=24,alpha=.5)

plt.show()
```


![06figures,subplots,axes和ticks对象_18_0](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/06figures,subplots,axes%E5%92%8Cticks%E5%AF%B9%E8%B1%A1_18_0.png)
    


### axes 对象

`subplot` 返回的是 `Axes` 对象，但是 `Axes` 对象相对于 `subplot` 返回的对象来说要更自由一点。`Axes` 对象可以放置在图像中的任意位置：


```python
plt.axes([0.1,0.1,.8,.8])
plt.xticks([]), plt.yticks([])
plt.text(0.6,0.6, 'axes([0.1,0.1,.8,.8])',ha='center',va='center',size=20,alpha=.5)

plt.axes([0.2,0.2,.3,.3])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'axes([0.2,0.2,.3,.3])',ha='center',va='center',size=16,alpha=.5)

plt.show()
```


![06figures,subplots,axes和ticks对象_21_0](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/06figures,subplots,axes%E5%92%8Cticks%E5%AF%B9%E8%B1%A1_21_0.png)
    

后面的 `Axes` 对象会覆盖前面的内容。