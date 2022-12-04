# Numpy入门[1]——Numpy简介
Numpy是Python的一个很重要的第三方库，很多其他科学计算的第三方库都是以Numpy为基础建立的。

Numpy的一个重要特性是它的数组计算。

## 数组上的数学操作
假如我们想将列表中的每个元素增加1，但列表不支持这样的操作（报错），可以使用numpy转换为数组


```python
import numpy as np
a = np.array([1, 2, 3, 4])
a+1

```




    array([2, 3, 4, 5])



两个数组相加


```python
b = np.array([2, 1, 2, 3])
a + b

```




    array([3, 3, 5, 7])



两个数组对应元素相乘


```python
a * b
```




    array([ 2,  2,  6, 12])




两个数组对应元素乘方


```python
a ** b
```




    array([ 1,  2,  9, 64], dtype=int32)



## 提取数组中的元素


提取第一个元素



```python
a[0]
```




    1



提取前两个元素


```python
a[:2]
```




    array([1, 2])



最后两个元素


```python
a[-2:]
```




    array([3, 4])



二者相加


```python
a[:2]+a[-2:]
```




    array([4, 6])



## 修改数组形状


查看`array`的形状


```python
a.shape
```




    (4,)



修改形状


```python
a.shape=2,2
a
```




    array([[1, 2],
           [3, 4]])



## 多维数组


`a`现在变成了一个二维数组，可以进行加法


```python
a + a
```




    array([[2, 4],
           [6, 8]])



乘法仍然是对应元素的乘积，<font color="red">并不是</font>按照矩阵乘法来计算：


```python
a * a
```




    array([[ 1,  4],
           [ 9, 16]])


