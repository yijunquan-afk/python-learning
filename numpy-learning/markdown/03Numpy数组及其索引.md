# Numpy入门[3]——Numpy数组及其索引

> 参考：
>
> [https://ailearning.apachecn.org/](https://ailearning.apachecn.org/)
>
> [Python直接使用plot()函数画图](https://blog.csdn.net/Sheenky/article/details/123976807)
>
> 使用Jupyter进行练习

先导入numpy：


```python
import numpy as np
```

## 产生数组

从列表产生数组


```python
mylist = [0, 1, 2, 3]
a = np.array(mylist)
a

```




    array([0, 1, 2, 3])



或者直接将列表传入


```python
a = np.array([1, 2, 3, 4])
a
```




    array([1, 2, 3, 4])



## 数组属性

查看类型：


```python
type(a)
```




    numpy.ndarray



查看数组中的数据类型：


```python
a.dtype
```




    dtype('int32')



查看每个元素所占的字节：


```python
a.itemsize
```




    4



查看形状，会返回一个元组，每个元素代表这一维的元素数目：


```python
a.shape
```




    (4,)



或者使用：


```python
np.shape(a)
```




    (4,)



查看元素数目：


```python
a.size
```




    4




```python
np.size(a)
```




    4



查看所有元素所占的空间：


```python
a.nbytes
```




    16



但事实上，数组所占的存储空间要比这个数字大，因为要用一个header来保存shape，dtype这样的信息。

查看数组维数：


```python
a.ndim
```




    1



## 使用fill方法设定初始值

可以使用`fill`方法将数组设定为指定值：


```python
a.fill(-1)
a
```




    array([-1, -1, -1, -1])




```python
a.fill(-4.8)
a
```




    array([-4, -4, -4, -4])



与列表不同，数组中要求所有元素的 dtype 是一样的，如果传入参数的类型与数组类型不一样，需要按照已有的类型进行转换。

## 索引和切片

索引第一个元素：


```python
a=np.array([0, 1, 2, 3])
a[0]
```




    0



修改第一个元素的值：


```python
a[0]=520
a
```




    array([520,   1,   2,   3])



切片，支持负索引：


```python
a=np.array([11, 12, 13, 14, 15])
a[1:3]
```




    array([12, 13])




```python
a[1:-2]
```




    array([12, 13])




```python
a[-4:3]
```




    array([12, 13])



省略参数：


```python
a[::2]
```




    array([11, 13, 15])




```python
a[-2:]
```




    array([14, 15])



假设我们记录一辆汽车表盘上每天显示的里程数：


```python
od = np.array([21000, 21180, 21240, 22100, 22400])
```

计算每天的旅程数如下：


```python
dist = od[1:] - od[:-1]
dist
```




    array([180,  60, 860, 300])



## 多维数组及其属性

`array`可以用于生成多维数组


```python
a = np.array([[ 0, 1, 2, 3],
           [10,11,12,13]])
a
```




    array([[ 0,  1,  2,  3],
           [10, 11, 12, 13]])




```python
# 查看形状
a.shape
```




    (2, 4)




```python
# 查看元素个数
a.size
```




    8




```python
# 查看维数
a.ndim
```




    2



## 多维数组索引

对于二维数组，可以传入两个数字来索引：


```python
a[1,3]
```




    13



其中，1是行索引，3是列索引，中间用逗号隔开，事实上，Python会将它们看成一个元组(1,3)，然后按照顺序进行对应。

可以利用索引给它赋值：


```python
a[1,3]=520
a
```




    array([[  0,   1,   2,   3],
           [ 10,  11,  12, 520]])



可以使用单个索引来索引一整行内容：


```python
a[1]
```




    array([ 10,  11,  12, 520])



## 多维数组切片


```python
a = np.array([[ 0, 1, 2, 3, 4, 5],
           [10,11,12,13,14,15],
           [20,21,22,23,24,25],
           [30,31,32,33,34,35],
           [40,41,42,43,44,45],
           [50,51,52,53,54,55]])
a
```




    array([[ 0,  1,  2,  3,  4,  5],
           [10, 11, 12, 13, 14, 15],
           [20, 21, 22, 23, 24, 25],
           [30, 31, 32, 33, 34, 35],
           [40, 41, 42, 43, 44, 45],
           [50, 51, 52, 53, 54, 55]])



得到第一行的第 4 和第 5 两个元素：


```python
a[0, 3:5]

```




    array([3, 4])



得到最后两行的最后两列：


```python
a[-2:,-2:]
```




    array([[44, 45],
           [54, 55]])




```python
a[4:,4:]
```




    array([[44, 45],
           [54, 55]])



得到第三列：


```python
a[:,2]
```




    array([ 2, 12, 22, 32, 42, 52])



取出3，5行的奇数列：


```python
a[2::2,::2]
```




    array([[20, 22, 24],
           [40, 42, 44]])



## 切片是引用

切片在内存中使用的是引用机制。


```python
a = np.array([0, 1, 2, 3, 4])
b = a[2:4]
print(b)

```

    [2 3]


引用机制意味着，Python并没有为 b 分配新的空间来存储它的值，而是让 b 指向了 a 所分配的内存空间，因此，改变 b 会改变 a 的值：


```python
b[0] = 10
a

```




    array([ 0,  1, 10,  3,  4])



而这种现象在列表中并不会出现：


```python
a = [1,2,3,4,5]
b = a[2:3]
b[0] = 13234
print(a)
```

    [1, 2, 3, 4, 5]


这样做的好处在于，对于很大的数组，不用大量复制多余的值，节约了空间。

缺点在于，可能出现改变一个值改变另一个值的情况。

一个解决方法是使用copy()方法产生一个复制，这个复制会申请新的内存：


```python
a = np.array([0,1,2,3,4])
b = a[2:4].copy()
b[0] = 10
a
```




    array([0, 1, 2, 3, 4])



## 花式索引

切片只能支持连续或者等间隔的切片操作，要想实现任意位置的操作，需要使用花式索引 `fancy slicing` 。

### 一维花式索引

与 range 函数类似，可以使用 arange 函数来产生等差数组。


```python
a = np.arange(0, 80, 10)
a
```




    array([ 0, 10, 20, 30, 40, 50, 60, 70])



花式索引需要指定索引位置：


```python
dict = [1, 2, -1]
b = a[dict]
b
```




    array([10, 20, 70])



可以使用布尔数组来花式索引：


```python
mask = np.array([0,1,1,0,0,1,0,0],
            dtype=bool)
a[mask]
```




    array([10, 20, 50])



或者用布尔表达式生成 mask，选出了所有大于0.5的值：


```python
from numpy.random import rand
x = rand(10)
print(x)
mask = x > 0.5
print(mask.dtype)
print(x[mask])
```

    [0.27839355 0.35630865 0.68024875 0.19407979 0.82448345 0.46120622
     0.83562489 0.98924664 0.7125346  0.27196064]
    bool
    [0.68024875 0.82448345 0.83562489 0.98924664 0.7125346 ]


## 二维花式索引


```python
a = np.array([[ 0, 1, 2, 3, 4, 5],
           [10,11,12,13,14,15],
           [20,21,22,23,24,25],
           [30,31,32,33,34,35],
           [40,41,42,43,44,45],
           [50,51,52,53,54,55]])
a
```




    array([[ 0,  1,  2,  3,  4,  5],
           [10, 11, 12, 13, 14, 15],
           [20, 21, 22, 23, 24, 25],
           [30, 31, 32, 33, 34, 35],
           [40, 41, 42, 43, 44, 45],
           [50, 51, 52, 53, 54, 55]])



对于二维花式索引，需要给定 `row` 和 `col` 的值：


```python
a[(0,1,2,3,4), (1,2,3,4,5)]
```




    array([ 1, 12, 23, 34, 45])




```python
# 最后三行的1，3，5列
a[-3:, [0,2,5]]
```




    array([[30, 32, 35],
           [40, 42, 45],
           [50, 52, 55]])



也可以使用mask进行索引：


```python
mask = np.array([1,0,1,0,0,1],
            dtype=bool)
a[mask, 2]
```




    array([ 2, 22, 52])



<font color="red">与切片不同，花式索引返回的是原对象的一个复制而不是引用。</font>

### 不完全索引


```python
y = a[:3]
y
```




    array([[ 0,  1,  2,  3,  4,  5],
           [10, 11, 12, 13, 14, 15],
           [20, 21, 22, 23, 24, 25]])




```python
# 使用花式索引取出第2，3，5行：
condition = np.array([0,1,1,0,1,0],
                 dtype=bool)
a[condition]
```




    array([[10, 11, 12, 13, 14, 15],
           [20, 21, 22, 23, 24, 25],
           [40, 41, 42, 43, 44, 45]])



## where语句

```python
where(array)
```

`where`函数会返回所有非零元素的索引

### 一维数组


```python
a = np.array([0, 12, 5, 20])
# 判断数组中的元素是不是大于10
a > 10
```




    array([False,  True, False,  True])



数组中所有大于10的元素的索引位置：


```python
np.where(a > 10)
```




    (array([1, 3], dtype=int64),)



注意到 where 的返回值是一个元组。

使用元组是由于 where 可以对多维数组使用，此时返回值就是多维的。

可以直接用 where 的返回值进行索引：


```python
loc = np.where(a > 10)
a[loc]
```




    array([12, 20])



### 多维数组


```python
a = np.array([[0, 12, 5, 20],
           [1, 2, 11, 15]]) 
print(a)
loc = np.where(a > 10)
loc
```

    [[ 0 12  5 20]
     [ 1  2 11 15]]





    (array([0, 0, 1, 1], dtype=int64), array([1, 3, 2, 3], dtype=int64))



返回结果是一个二维的元组，每一维代表这一维的索引值：

可以直接用来索引a：


```python
a[loc]
```




    array([12, 20, 11, 15])



或者可以这样：


```python
rows, cols = np.where( a > 10)
print(rows)
print(cols)
a[rows,cols]
```

    [0 0 1 1]
    [1 3 2 3]





    array([12, 20, 11, 15])



另一个例子


```python
c = np.arange(25)
c.shape= 5,5
c
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24]])




```python
c > 12
```




    array([[False, False, False, False, False],
           [False, False, False, False, False],
           [False, False, False,  True,  True],
           [ True,  True,  True,  True,  True],
           [ True,  True,  True,  True,  True]])




```python
np.where( c > 12 )
```




    (array([2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4], dtype=int64),
     array([3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4], dtype=int64))


