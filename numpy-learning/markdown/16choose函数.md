# Numpy入门[16]——choose函数实现条件筛选
> 参考：
>
> + [https://ailearning.apachecn.org/](https://ailearning.apachecn.org/)
> + [numpy高级函数操作之——select、choose](https://blog.csdn.net/qq_27825451/article/details/82698929)
>
> 使用Jupyter进行练习


借助`numpy.choose()`方法，我们可以通过将包含要选择的行号索引的参数作为数组传递，从多维数组中选择元素。

对于数组，有时候需要进行类似 `switch` 和 `case` 进行条件选择，此时使用 choose 函数十分方便：

```python
def choose(a, choices, out=None, mode='raise')
```

参数 a ：它必须是一个 int 型的 数组，并且 a 中的元素，必须是0~n-1之间的数，这里的n表示的就是数组choices数组最外层的维度数。

choices：表示的是要操作的数组，要注意的是choices的数组的维度是一定要和a进行匹配的，如果匹配不了，会出现错误。

参数out：接收运算结果的数组，它的维度一定要和 a 是一样的，是可选参数。

参数mode：

+ 默认的是raise，表示的是a数组中的元素不能超过 n 

+ clip：将 a 中的 元素 如果小于0，则将其变为0，如果大于n-1，则变为n-1

+ wrap：将a中的值 value变为value mod n，即值除以n的余数。


```python
import numpy as np
a = np.array([[2,0,1],
              [2,1,0],
              [1,2,2]])
choice = np.array([])

np.choose(a, [[0, 1, 2], 
              [10, 11, 12],
              [20, 21, 22]])
```




    array([[20,  1, 12],
           [20, 11,  2],
           [10, 21, 22]])



在上面的例子中，a中第一行第一列元素映射为choice中第三行（2）第一列元素，第一行第二列元素映射为choice中第一行（0）第二列元素，映射的是行下标。

事实上， choose 不仅仅能接受下标参数，还可以接受下标所在的位置：


```python
i0 = np.array([[0,1,2],
               [3,4,5],
               [6,7,8]])
i2 = np.array([[20,21,22],
               [23,24,25],
               [26,27,28]])
a = np.array([[1,0,1],
              [2,1,0],
              [1,2,2]])

np.choose(a, [i0, 10, i2])
```




    array([[10,  1, 10],
           [23, 10,  5],
           [10, 27, 28]])



这里，control 传入第一个 1 对应的是 10，传入的第一个 0 对应于 i0 相应位置的值即 1，剩下的以此类推。

下面的例子将数组中所有小于 10 的值变成了 10。


```python
a = np.array([[ 0, 1, 2], 
              [10,11,12], 
              [20,21,22]])

a < 10
```




    array([[ True,  True,  True],
           [False, False, False],
           [False, False, False]])




```python
# False(0)对应的是a中相应的元素，True(1)对应的是10
np.choose(a < 10, (a, 10))
```




    array([[10, 10, 10],
           [10, 11, 12],
           [20, 21, 22]])



下面的例子将数组中所有小于 10 的值变成了 10，大于 15 的值变成了 15。


```python
a = np.array([[ 0, 1, 2], 
              [10,11,12], 
              [20,21,22]])

lt = a < 10
gt = a > 15

choice = lt + 2 * gt
choice
```




    array([[1, 1, 1],
           [0, 0, 0],
           [2, 2, 2]])




```python
np.choose(choice, (a, 10, 15))
```




    array([[10, 10, 10],
           [10, 11, 12],
           [15, 15, 15]])


