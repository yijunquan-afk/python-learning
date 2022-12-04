# Numpy入门[2]——Matplotlib 基础

> 参考：
>
> [https://ailearning.apachecn.org/](https://ailearning.apachecn.org/)
>
> [Python直接使用plot()函数画图](https://blog.csdn.net/Sheenky/article/details/123976807)
>
> 使用Jupyter进行练习

在使用Numpy之前，需要了解一些画图的基础。

Matplotlib是一个类似Matlab的工具包，主页地址为

http://matplotlib.org

导入 matplotlib 和 numpy：


```python
import numpy as np
import matplotlib.pyplot as plt
```

## plot二维图
```python
plot(y)
plot(x, y)
plot(x, y, format_string)
```

只给定 y 值，默认以下标为 x 轴：


```python
# 等距分
x = np.linspace(0, 2*np.pi,50)
plt.plot(np.sin(x))
```




    [<matplotlib.lines.Line2D at 0x25593113dc0>]




![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_4_1.png)
    


给定 x 和 y 值：


```python
plt.plot(x,np.sin(x))
```




    [<matplotlib.lines.Line2D at 0x2559318d040>]




![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_6_1.png)
    


多条数据线：



```python
plt.plot(x, np.sin(x), x, np.sin(2*x))

```




    [<matplotlib.lines.Line2D at 0x25593231d60>,
     <matplotlib.lines.Line2D at 0x25593231d90>]




![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_8_1.png)
    


使用字符串，给定线条参数：
![image-20221128154653101](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/image-20221128154653101.png)

![image-20221128154711826](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/image-20221128154711826.png)


```python
plt.plot(x,np.sin(x),'r-^')
```




    [<matplotlib.lines.Line2D at 0x255933e4b80>]




​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_10_1.png)
​    


多线条:


```python
plt.plot(x, np.sin(x), "b-o",x, np.sin(2*x),"r-^")
```




    [<matplotlib.lines.Line2D at 0x255932d87f0>,
     <matplotlib.lines.Line2D at 0x255932d88b0>]




​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_12_1.png)
​    


## scatter 散点图
```python
scatter(x, y)
scatter(x, y, size)
scatter(x, y, size, color)
```

画二维散点图


```python
plt.plot(x,np.sin(x),"bo")
```




    [<matplotlib.lines.Line2D at 0x25592028ca0>]




​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_15_1.png)
​    


可以使用 scatter 达到同样的效果：


```python
plt.scatter(x, np.sin(x))
```




    <matplotlib.collections.PathCollection at 0x25591e62940>




![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_17_1.png)
    


scatter函数与Matlab的用法相同，还可以指定它的大小，颜色等参数：


```python
from numpy import random
# 产生随机数组
x = random.rand(200)
y = random.rand(200)
size = random.rand(200) * 30
color = random.rand(200)
plt.scatter(x, y, size, color)
# 显示颜色条
plt.colorbar()

```




    <matplotlib.colorbar.Colorbar at 0x2558f559af0>




​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_19_1.png)
​    


## 多图
使用figure()命令产生新的图像：


```python
t = np.linspace(0, 2 * np.pi, 50)
x = np.sin(t)
y = np.cos(t)
plt.figure()
plt.plot(x)
plt.figure()
plt.plot(y)
```




    [<matplotlib.lines.Line2D at 0x2559333b970>]




![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_21_1.png)
    


![02Matlpotlib基础_21_2](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_21_2.png)
    


或者使用 subplot 在一幅图中画多幅子图：
```
subplot(row, column, index)
```


```python
plt.subplot(1,2,1)
plt.plot(x)
plt.subplot(1,2,2)
plt.plot(y)
```




    [<matplotlib.lines.Line2D at 0x2559344e4f0>]




​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_23_1.png)
​    


## 标签
可以在 plot 中加入 label ，使用 legend 加上图例：


```python
plt.plot(x, label='sin')
plt.plot(y, label='cos')
plt.legend()
```




    <matplotlib.legend.Legend at 0x255946fd430>




​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_25_1.png)
​    


或者直接在 legend中加入：


```python
plt.plot(x)
plt.plot(y)
plt.legend(['sin','cos'])
```




    <matplotlib.legend.Legend at 0x255948c3640>




​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_27_1.png)
​    


## 坐标轴，标题，网格

可以设置坐标轴的标签和标题：



```python
plt.plot(x,np.sin(x))
plt.xlabel("radians")
plt.ylabel("amplitude",fontsize="large")
plt.title('Sin(x)')
# 设置网格
plt.grid()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_30_0.png)
​    


## 清除、关闭图像

+ 清除已有图像使用：`clf()`
+ 关闭当前图像：`close()`
+ 关闭所有图像：`close('all')`

## 从脚本中运行

在脚本中使用 plot 时，通常图像是不会直接显示的，需要增加 show() 选项，只有在遇到 show() 命令之后，图像才会显示。

## 直方图
从高斯分布随机生成1000个点得到的直方图：


```python
plt.hist(np.random.randn(1000))
```




    (array([  2.,   5.,  33., 147., 266., 298., 171.,  68.,   9.,   1.]),
     array([-4.06787487, -3.28558599, -2.50329712, -1.72100825, -0.93871938,
            -0.15643051,  0.62585836,  1.40814724,  2.19043611,  2.97272498,
             3.75501385]),
     <BarContainer object of 10 artists>)




​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02Matlpotlib%E5%9F%BA%E7%A1%80_34_1.png)
​    

