# Matplotlib入门[01]——Pyplot

> 参考：
>
> + [https://ailearning.apachecn.org/](https://ailearning.apachecn.org/)
> + [Matplotlib官网](https://matplotlib.org/)
>
> 使用Jupyter进行练习

![Logo image](https://matplotlib.org/stable/_static/images/logo2.svg)





## Matplotlib简介

**`matplotlib`** 是一个 **`Python`** 的 `2D` 图形包。

在线文档：[http://matplotlib.org](http://matplotlib.org/) ，提供了 [Examples](http://matplotlib.org/examples/index.html), [FAQ](http://matplotlib.org/faq/index.html), [API](http://matplotlib.org/contents.html), [Gallery](http://matplotlib.org/gallery.html)，其中 [Gallery](http://matplotlib.org/gallery.html) 是很有用的一个部分，因为它提供了各种画图方式的可视化，方便用户根据需求进行选择。



```python
import numpy as np
import matplotlib.pyplot as plt
```

下文中，以 `plt` 作为 `matplotlib.pyplot` 的省略。

## plt.plot() 函数

### 举例


```python
# plot函数可以用来绘图
plt.plot([1,2,3,4])
plt.ylabel('some numbers')

plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/01Pyplot%E6%95%99%E7%A8%8B_7_0.png)
​    


### 基本用法

`plot` 函数基本的用法有以下四种：

默认参数

- `plt.plot(x,y)`

指定参数

- `plt.plot(x,y, format_str)`

默认参数，`x` 为 `0~N-1`

- `plt.plot(y)`

指定参数，`x` 为 `0~N-1`

- `plt.plot(y, format_str)`

因此，在上面的例子中，我们没有给定 `x` 的值，所以其默认值为 `[0,1,2,3]`。

传入 `x` 和 `y`：


```python
plt.plot([1,2,3,4], [1,4,9,16])
plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/01Pyplot%E6%95%99%E7%A8%8B_10_0.png)
​    


### 字符参数

可以用字符来指定绘图的格式：

表示颜色的字符参数有：

| 字符  | 颜色          |
| ----- | ------------- |
| `‘b’` | 蓝色，blue    |
| `‘g’` | 绿色，green   |
| `‘r’` | 红色，red     |
| `‘c’` | 青色，cyan    |
| `‘m’` | 品红，magenta |
| `‘y’` | 黄色，yellow  |
| `‘k’` | 黑色，black   |
| `‘w’` | 白色，white   |

表示类型的字符参数有：

| 字符   | 类型       | 字符   | 类型      |
| ------ | ---------- | ------ | --------- |
| `'-'`  | 实线       | `'--'` | 虚线      |
| `'-.'` | 虚点线     | `':'`  | 点线      |
| `'.'`  | 点         | `','`  | 像素点    |
| `'o'`  | 圆点       | `'v'`  | 下三角点  |
| `'^'`  | 上三角点   | `'<'`  | 左三角点  |
| `'>'`  | 右三角点   | `'1'`  | 下三叉点  |
| `'2'`  | 上三叉点   | `'3'`  | 左三叉点  |
| `'4'`  | 右三叉点   | `'s'`  | 正方点    |
| `'p'`  | 五角点     | `'*'`  | 星形点    |
| `'h'`  | 六边形点1  | `'H'`  | 六边形点2 |
| `'+'`  | 加号点     | `'x'`  | 乘号点    |
| `'D'`  | 实心菱形点 | `'d'`  | 瘦菱形点  |
| `'_'`  | 横线点     |        |           |

例如画出红色圆点蓝色虚线：


```python
plt.plot([1,2,3,4], [1,4,9,16], 'b--',
         [1,2,3,4], [1,4,9,16], 'ro')
plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/01Pyplot%E6%95%99%E7%A8%8B_13_0.png)
​    



### 显示范围

与 MATLAB 类似，这里可以使用 `axis` 函数指定坐标轴显示的范围：
```python
plt.axis([xmin, xmax, ymin, ymax])
```


```python
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# 指定 x 轴显示区域为 0-6，y 轴为 0-20
plt.axis([0,6,0,20])
plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/01Pyplot%E6%95%99%E7%A8%8B_16_0.png)
​    


### 传入Numpy数组

之前传给 `plot` 的参数都是列表，事实上，向 `plot` 中传入 `numpy` 数组是更常用的做法。事实上，如果传入的是列表，`matplotlib` 会在内部将它转化成数组再进行处理：


```python
t = np.arange(0., 5., 0.2)

# 不需要使用多个 plot 函数来画多组数组
# 只需要可以将这些组合放到一个 plot 函数中去即可。
plt.plot(t, t, 'r--', 
         t, t**2, 'bs', 
         t, t**3, 'g^')

plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/01Pyplot%E6%95%99%E7%A8%8B_19_0.png)
​    


### 线条属性

还可以通过关键词来改变线条的性质，例如 `linwidth` 可以改变线条的宽度，`color` 可以改变线条的颜色：


```python
x = np.linspace(-np.pi,np.pi)
y = np.sin(x)

plt.plot(x, y, linewidth=2.0, color='r')

plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/01Pyplot%E6%95%99%E7%A8%8B_22_0.png)
​    


### 使用plt.plot() 的返回值来设置线条属性

`plot` 函数返回一个 `Line2D` 对象组成的列表，每个对象代表输入的一对组合，例如：

- line1, line2 为两个 Line2D 对象

  `line1, line2 = plt.plot(x1, y1, x2, y2)`

- 返回 3 个 Line2D 对象组成的列表

  `lines = plt.plot(x1, y1, x2, y2, x3, y3)`

可以使用这个返回值来对线条属性进行设置：


```python
# 加逗号 line 中得到的是 line2D 对象，不加逗号得到的是只有一个 line2D 对象的列表
line, = plt.plot(x, y, 'r-')

# 将抗锯齿关闭
line.set_antialiased(False)

plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/01Pyplot%E6%95%99%E7%A8%8B_24_0.png)
​    


### plt.setp() 修改线条性质

更方便的做法是使用 `plt` 的 `setp` 函数：


```python
lines = plt.plot(x, y)

# 使用键值对
plt.setp(lines, color='r', linewidth=2.0)

plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/01Pyplot%E6%95%99%E7%A8%8B_27_0.png)
​    


可以设置的属性有很多，可以使用 plt.setp(lines) 查看 lines 可以设置的属性，各属性的含义可参考 matplotlib 的文档。


```python
plt.setp(lines)
```

      agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array
      alpha: scalar or None
      animated: bool
      antialiased or aa: bool
      clip_box: `.Bbox`
      clip_on: bool
      clip_path: Patch or (Path, Transform) or None
      color or c: color
      contains: unknown
      dash_capstyle: `.CapStyle` or {'butt', 'projecting', 'round'}
      dash_joinstyle: `.JoinStyle` or {'miter', 'round', 'bevel'}
      dashes: sequence of floats (on/off ink in points) or (None, None)
      data: (2, N) array or two 1D arrays
      drawstyle or ds: {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default'
      figure: `.Figure`
      fillstyle: {'full', 'left', 'right', 'bottom', 'top', 'none'}
      gid: str
      in_layout: bool
      label: object
      linestyle or ls: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
      linewidth or lw: float
      marker: marker style string, `~.path.Path` or `~.markers.MarkerStyle`
      markeredgecolor or mec: color
      markeredgewidth or mew: float
      markerfacecolor or mfc: color
      markerfacecoloralt or mfcalt: color
      markersize or ms: float
      markevery: None or int or (int, int) or slice or list[int] or float or (float, float) or list[bool]
      path_effects: `.AbstractPathEffect`
      picker: float or callable[[Artist, Event], tuple[bool, dict]]
      pickradius: float
      rasterized: bool
      sketch_params: (scale: float, length: float, randomness: float)
      snap: bool or None
      solid_capstyle: `.CapStyle` or {'butt', 'projecting', 'round'}
      solid_joinstyle: `.JoinStyle` or {'miter', 'round', 'bevel'}
      transform: `matplotlib.transforms.Transform`
      url: str
      visible: bool
      xdata: 1D array
      ydata: 1D array
      zorder: float


## 子图

figure() 函数会产生一个指定编号为 num 的图：
```python
plt.figure(num) 
```
使用 `subplot` 可以在一副图中生成多个子图，其参数为：

```py
plt.subplot(numrows, numcols, fignum) 
```

当 `numrows * numcols < 10` 时，中间的逗号可以省略，因此 `plt.subplot(211)` 就相当于 `plt.subplot(2,1,1)`。


```python
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
# 两行一列第一个
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# 两行一列第二个
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/01Pyplot%E6%95%99%E7%A8%8B_32_0.png)
​    


## 图形上加上文字

`plt.hist()` 可以用来画直方图。


```python
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/01Pyplot%E6%95%99%E7%A8%8B_35_0.png)
​    


对于这幅图形，我们使用 `xlabel` ，`ylabel`，`title`，`text` 方法设置了文字，其中：

- `xlabel` ：x 轴标注
- `ylabel` ：y 轴标注
- `title` ：图形标题
- `text` ：在指定位置放入文字

输入特殊符号支持使用 `Tex` 语法，用 `$<some Tex code>$` 隔开。

除了使用 `text` 在指定位置标上文字之外，还可以使用 `annotate` 函数进行注释，`annotate` 主要有两个参数：

- `xy` ：注释位置
- `xytext` ：注释文字位置


```python
ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.ylim(-2,2)
plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/01Pyplot%E6%95%99%E7%A8%8B_37_0.png)
​    

