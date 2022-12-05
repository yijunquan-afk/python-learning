# Numpy入门[15]——ufunc对象
> 参考：
>
> [https://ailearning.apachecn.org/](https://ailearning.apachecn.org/)
>
> 使用Jupyter进行练习

Numpy 有两种基本对象：`ndarray (N-dimensional array object)` 和 `ufunc (universal function object)`。ndarray 是存储单一数据类型的多维数组，而 ufunc 则是能够对数组进行处理的函数。

例如，我们之前所接触到的二元操作符对应的 Numpy 函数，如 add，就是一种 ufunc 对象，它可以作用于数组的每个元素。


```python
import numpy as np

```


```python
a = np.array([0, 1, 2])
b = np.array([3, 4, 5])
np.add(a,b)
```




    array([3, 5, 7])



查看支持的方法：


```python
dir(np.add)
```




    ['__call__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__name__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'accumulate',
     'at',
     'identity',
     'nargs',
     'nin',
     'nout',
     'ntypes',
     'outer',
     'reduce',
     'reduceat',
     'signature',
     'types']



除此之外，大部分能够作用于数组的数学函数如三角函数等，都是 ufunc 对象。

特别地，对于二元操作符所对应的 ufunc 对象，支持以下方法：

## reduce方法

```python
op.reduce(a) 
```
将`op`沿着某个轴应用，使得数组 `a` 的维数降低一维。

add 作用到一维数组上相当于求和。

$$
\begin{align} 
y & = add.recuce(a) \\ 
  & = a[0] + a[1] + ... + a[N-1] \\ 
  & = \sum_{n=0}^{N-1} a[n] 
\end{align}
$$


```python
a = np.array([1,2,3,4])

np.add.reduce(a)
```




    10



多维数组默认只按照第一维进行运算：


```python
a = np.array([[1,2,3],[4,5,6]])

np.add.reduce(a)
```




    array([5, 7, 9])



指定维度：


```python
np.add.reduce(a, 1)
```




    array([ 6, 15])



作用于字符串：


```python
a = np.array(['ab', 'cd', 'ef'], object)

np.add.reduce(a)
```




    'abcdef'



逻辑运算：


```python
a = np.array([1,1,0,1])

np.logical_and.reduce(a)
```




    False




```python
np.logical_or.reduce(a)
```




    True



## accumulate方法

```python
op.accumulate(a)
```
accumulate 可以看成保存 reduce 每一步的结果所形成的数组。
$$
\begin{align} y & = add.accumulate(a) \\ & = \left[\sum_{n=0}^{0} a[n], \sum_{n=0}^{1} a[n], ..., \sum_{n=0}^{N-1} a[n]\right] \end{align}
$$


```python
a = np.array([1,2,3,4])

np.add.accumulate(a)
```




    array([ 1,  3,  6, 10], dtype=int32)




```python
a = np.array(['ab', 'cd', 'ef'], object)

np.add.accumulate(a)
```




    array(['ab', 'abcd', 'abcdef'], dtype=object)




```python
a = np.array([1,1,0,1])

np.logical_and.accumulate(a)
```




    array([ True,  True, False, False])




```python
np.logical_or.accumulate(a)

```




    array([ True,  True,  True,  True])



## reduceat方法

op.reduceat(a, indices) 

`reduceat` 方法将操作符运用到指定的下标上，返回一个与 `indices` 大小相同的数组：

$$
\begin{align} y & = add.reduceat(a, indices) \\ & = \left[\sum_{n=indice[0]}^{indice[1]-1} a[n], \sum_{n=indice[1]}^{indice[2]-1} a[n], ..., \sum_{n=indice[M-1]}^{N-1} a[n]\right] \end{align}
$$


```python
a = np.array([5, 10, 20, 30, 40, 50])
indices = np.array([1,4])

# (a[1]+a[2]+a[3],a[4]+a[5])
np.add.reduceat(a, indices)

```




    array([60, 90], dtype=int32)



## outer方法

```python
op.outer(a, b) 
```

对于 `a` 中每个元素，将 `op` 运用到它和 `b` 的每一个元素上所得到的结果：


```python
a = np.array([0,1])
b = np.array([1,2,3])

np.add.outer(a, b)
```




    array([[1, 2, 3],
           [2, 3, 4]])



注意有顺序的区别：


```python
np.add.outer(b, a)
```




    array([[1, 2],
           [2, 3],
           [3, 4]])


