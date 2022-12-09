# Python基础学习
>
> 参考资料：
> 
> + [AILearning](https://ailearning.apachecn.org/#/docs/da/064)
> + [菜鸟教程](https://www.runoob.com/python3/python-comprehensions.html)
> + [Python中的可变和不可变类型](https://blog.csdn.net/qq_32334103/article/details/123690543)
> 
> + [python面向对象：生成器](https://blog.csdn.net/zl202111/article/details/124101232)
> 
> 使用Jupyter进行练习
>
> python-version: 3.9.3



## 一、Python数据类型

### 常用数据类型
| 类型      | 例子                     |
| --------- | ------------------------ |
| 整数      | `-100`                   |
| 浮点数    | `3.1416`                 |
| 字符串    | `'hello'`                |
| 列表      | `[1, 1.2, 'hello']`      |
| 字典      | `{'dogs': 5, 'pigs': 3}` |
| Numpy数组 | `array([1, 2, 3])`       |


### 其他类型
| 类型       | 例子                      |
| ---------- | ------------------------- |
| 布尔型     | `True, False`             |
| 元组       | `('ring', 1000)`          |
| 集合       | `{1, 2, 3}`               |
| Pandas类型 | `DataFrame, Series`       |
| 自定义     | `Object Oriented Classes` |

## 二、数字

### 整型 Integers


```python
# 查看类型
a = 1
print("整型类型：",type(a))
# 整性运算，加减乘除
print("整型加法运算：2 + 2 = ", 2 + 2)
print("整型减法运算：2 - 3 = ", 2 - 3)
print("整型乘法运算：2 * 3 = ", 2 * 3)
# 在Python 2.7中，整型的运算结果只能返回整型，除法的结果也不例外
# 在Python3.9.3中会将结果返回为浮点数
print("整型除法运算：4 / 4 = ", 4 / 4)
```

    整型类型： <class 'int'>
    整型加法运算：2 + 2 =  4
    整型减法运算：2 - 3 =  -1
    整型乘法运算：2 * 3 =  6
    整型除法运算：4 / 4 =  1.0
    


```python
# 其他运算
print("整型幂指数：2 ** 5 = ", 2 ** 5)
print("整型取余：20 % 3 = ", 20 % 3)
```

    整型幂指数：2 ** 5 =  32
    整型取余：20 % 3 =  2
    

整型数字的最大最小值：

在 32 位系统中，一个整型 4 个字节，最小值 `-2,147,483,648`，最大值 `2,147,483,647`。

在 64 位系统中，一个整型 8 个字节，最小值 `-9,223,372,036,854,775,808`，最大值 `9,223,372,036,854,775,807`。


```python
import platform   
import sys
print("此系统为：",platform.architecture())
print("此系统中，整型的最大值为：", sys.maxsize)
```

    此系统为： ('64bit', 'WindowsPE')
    此系统中，整型的最大值为： 9223372036854775807
    

### 浮点数 Floating Point Numbers


```python
a = 5.20
print("浮点数类型: ",type(a))
# 浮点数与整数进行运算时，返回的仍然是浮点数：
print("浮点数与整数相除: 1.0 / 5 = ", 1.0 / 5)
# 其余运算与整数差不多
print("浮点数加法运算：2.0 + 2.0 = ", 2.0 + 2.0)
print("浮点数减法运算：2.0 - 3.0 = ", 2.0 - 3.0)
print("浮点数乘法运算：2.0 * 3.0 = ", 2.0 * 3.0)
print("浮点数除法运算：4.0 / 4.0 = ", 4.0 / 4.0)
```

    浮点数类型:  <class 'float'>
    浮点数与整数相除: 1.0 / 5 =  0.2
    浮点数加法运算：2.0 + 2.0 =  4.0
    浮点数减法运算：2.0 - 3.0 =  -1.0
    浮点数乘法运算：2.0 * 3.0 =  6.0
    浮点数除法运算：4.0 / 4.0 =  1.0
    

**Python**的浮点数标准与**C**，**Java**一致，都是[IEEE 754 floating point standard](http://en.wikipedia.org/wiki/IEEE_floating_point)。

注意看 `3.4 - 3.2` 的结果并不是我们预期的`0.2`，这是因为浮点数本身储存方式引起的，浮点数本身会存在一点误差。

事实上，**Python** 中储存的值为'0.199999999999999733546474089962430298328399658203125'，因为这是最接近0.2的浮点数。


```python
print(3.4 - 3.2)
print('{:.2}'.format(3.4 - 3.2))
print('{:.52}'.format(3.4 - 3.2))
```

    0.19999999999999973
    0.2
    0.199999999999999733546474089962430298328399658203125
    

可以用`sys.float_info`来查看浮点数的信息：


```python
print(sys.float_info)
print("浮点数的最大值：",sys.float_info.max)
print("浮点数最接近0的数：",sys.float_info.min)
print("浮点数的精度：",sys.float_info.epsilon)
```

    sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
    浮点数的最大值： 1.7976931348623157e+308
    浮点数最接近0的数： 2.2250738585072014e-308
    浮点数的精度： 2.220446049250313e-16
    

### 复数 Complex Numbers

**Python** 使用 `j` 来表示复数的虚部：


```python
a = 5 + 20j
print("复数类型：",type(a))
print("实部：",a.real)
print("虚部：",a.imag)
print("共轭复数：",a.conjugate())
```

    复数类型： <class 'complex'>
    实部： 5.0
    虚部： 20.0
    共轭复数： (5-20j)
    

### 复杂运算



```python
# 复杂运算
1 + 2 - (3 * 4 / 6) ** 5 + 7 % 5
```




    -27.0



在**Python**中运算是有优先级的，优先级即算术的先后顺序，比如“先乘除后加减”和“先算括号里面的”都是两种优先级的规则，优先级从高到低排列如下：

- `( )` 括号
- `**` 幂指数运算
- `* / // %` 乘，除，整数除法，取余运算
- `+-` 加减


```python
# 整数除法，返回的是比结果小的最大整数值：
print("整除：12.3 // 5.2 = ", 12.3 // 5.2)
print("整除：12.3 // -4 = ", 12.3 // -4)
```

    整除：12.3 // 5.2 =  2.0
    整除：12.3 // -4 =  -4.0
    

### 简单的数学函数


```python
print("绝对值：abs(-12.4) = " , abs(12.4))
print("取整：round(2.6) = ", round(2.6))
print("最大值：max(1, 2, 3, 4) = ", max(1, 2, 3, 4))
print("最小值：min(1, 2, 3, 4) = ", min(1, 2, 3, 4))
```

    绝对值：abs(-12.4) =  12.4
    取整：round(2.6) =  3
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In [286], line 3
          1 print("绝对值：abs(-12.4) = " , abs(12.4))
          2 print("取整：round(2.6) = ", round(2.6))
    ----> 3 print("最大值：max(1, 2, 3, 4) = ", max(1, 2, 3, 4))
          4 print("最小值：min(1, 2, 3, 4) = ", min(1, 2, 3, 4))
    

    TypeError: 'int' object is not callable


### 变量名覆盖

<font color="red">不要用内置的函数来命名变量，否则会出现意想不到的结果：</font>


```python
max = 1
print(type(max))
max(4, 5)
```

    <class 'int'>
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In [62], line 3
          1 max = 1
          2 print(type(max))
    ----> 3 max(4, 5)
    

    TypeError: 'int' object is not callable


### 类型转换


```python
print("浮点数转整型，只保留整数部分: int(12.345) = ", int(12.345))
print("浮点数转整型，只保留整数部分: int(-1.23) = ", int(-1.23))
print("整型转浮点数: float(2) = ", float(2))
```

    浮点数转整型，只保留整数部分: int(12.345) =  12
    浮点数转整型，只保留整数部分: int(-1.23) =  -1
    整型转浮点数: float(2) =  2.0
    

### 其他表示

除了10进制外，整数还有其他类型的表示方法。


```python
print("科学计数法：1e-6 = ", 1e-6)
# 16进制，前面加0x修饰，后面使用数字0-9A-F：
print("16进制：0xFF = ", 0xFF)
# 8进制，前面加0o修饰，后面使用数字0-7：
print("八进制：067 = ", 0o67)
# 2进制，前面加0b修饰，后面使用数字0或1：
print("二进制：0b1010101 = ", 0b1010101)

```

    科学计数法：1e-6 =  1e-06
    16进制：0xFF =  255
    八进制：067 =  55
    二进制：0b1010101 =  85
    

### 原地计算In-place
Python可以使用下面的形式进行原地计算：



```python
b = 2.5
b += 2
print(b)
b *= 2
print(b)
b -= 3
print(b)

```

    4.5
    9.0
    6.0
    

### 布尔型 Boolean Data Type

布尔型可以看成特殊的二值变量，其取值为`True`和`False`：


```python
q = True
print("布尔型：",type(q))
# 可以用表达式构建布尔型变量
print("表达式构建布尔型变量：",1 > 2)
# 常用的比较符号包括：<, >, <=, >=, ==, != 
# Python支持链式比较
x = 2
print("链式比较：1 <  x <= 3",1 <  x <= 3)
```

    布尔型： <class 'bool'>
    表达式构建布尔型变量： False
    链式比较：1 <  x <= 3 True
    

## 三、字符串

### 生成字符串

Python中可以使用一对单引号''或者双引号""生成字符串


```python
print("单引号生成字符串：",'hello python')
print("双引号生成字符串：","hello python")
```

    单引号生成字符串： hello python
    双引号生成字符串： hello python
    

Python 用一对 """ 或者 ''' 来生成多行字符串：


```python
a = """i love
you."""
print(a)
```

    i love
    you.
    

储存时，两行字符间加上一个换行符 '\n'


```python
a
```




    'i love\nyou.'



### 简单操作


```python
s1 = 'hello'
s2 = 'python'
print("加法：", s1, "+", s2, "=", s1+s2)
print("字符串与数字相乘：" , s1 , " * 3" , " = " , s1 * 3)
print(s1 , "的长度为：", len(s1))

```

    加法： hello + python = hellopython
    字符串与数字相乘： hello  * 3  =  hellohellohello
    hello 的长度为： 5
    

### 字符串方法

Python是一种面向对象的语言，面向对象的语言中一个必不可少的元素就是方法，而字符串是对象的一种，所以有很多可用的方法。

跟很多语言一样，Python使用以下形式来调用方法：

```
对象.方法(参数)
```

#### 分割

`s.split()`: 将s按照空格（包括多个空格，制表符\t，换行符\n等）分割，并返回所有分割得到的字符串。



```python
line = "1 2 3 4  5"
numbers = line.split()
print(numbers)
```

    ['1', '2', '3', '4', '5']
    

`s.split(sep)`: 以给定的sep为分隔符对s进行分割。


```python
line = "1,2,3,4,5"
numbers = line.split(',')
print(numbers)
```

    ['1', '2', '3', '4', '5']
    

#### 连接

`s.join(str_sequence)`: 以s为连接符将字符串序列`str_sequence`中的元素连接起来，并返回连接后得到的新字符串


```python
s = ' '
s.join(numbers)
```




    '1 2 3 4 5'




```python
s = ','
s.join(numbers)
```




    '1,2,3,4,5'



#### 替换

`s.replace(part1, part2)`: 将字符串s中指定的部分part1替换成想要的部分part2，并返回新的字符串。


```python
s = "hello world"
print(s.replace('world', 'python'))
# s的值并没有变化
print(s)
```

    hello python
    hello world
    

#### 大小写转换

`s.upper()`: 方法返回一个将s中的字母全部大写的新字符串。

`s.lower()`: 方法返回一个将s中的字母全部小写的新字符串。


```python
print("hello world".upper())
print("YJQ".lower())
```

    HELLO WORLD
    yjq
    

#### 去除多余空格

`s.strip()`返回一个将s两端的多余空格除去的新字符串。

`s.lstrip()`返回一个将s开头的多余空格除去的新字符串。

`s.rstrip()`返回一个将s结尾的多余空格除去的新字符串。


```python
s = "  hello world   "
print("去除两端空格: ", s.strip())
print("去除开头空格: ", s.lstrip())
print("去除结尾空格: ", s.rstrip())
```

    去除两端空格:  hello world
    去除开头空格:  hello world   
    去除结尾空格:    hello world
    

#### 更多方法


```python
dir(s)
```




    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rmod__',
     '__rmul__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'capitalize',
     'casefold',
     'center',
     'count',
     'encode',
     'endswith',
     'expandtabs',
     'find',
     'format',
     'format_map',
     'index',
     'isalnum',
     'isalpha',
     'isascii',
     'isdecimal',
     'isdigit',
     'isidentifier',
     'islower',
     'isnumeric',
     'isprintable',
     'isspace',
     'istitle',
     'isupper',
     'join',
     'ljust',
     'lower',
     'lstrip',
     'maketrans',
     'partition',
     'removeprefix',
     'removesuffix',
     'replace',
     'rfind',
     'rindex',
     'rjust',
     'rpartition',
     'rsplit',
     'rstrip',
     'split',
     'splitlines',
     'startswith',
     'strip',
     'swapcase',
     'title',
     'translate',
     'upper',
     'zfill']



### 使用() 或者\ 换行

当代码太长或者为了美观起见时，可以使用两种方法来将一行代码转为多行代码：
+ `()`
+ `\`


```python
a = ("hello, world. "
    "it's a nice day. "
    "my name is xxx")
a
```




    "hello, world. it's a nice day. my name is xxx"




```python
a = "hello, world. " \
    "it's a nice day. " \
    "my name is xxx"
a
```




    "hello, world. it's a nice day. my name is xxx"



### 强制转换为字符串

- `str(ob)`强制将`ob`转化成字符串。
- `repr(ob)`也是强制将`ob`转化成字符串。

`str()`主要用来为终端用户输出一些信息，而`repr()`主要用来调试。


```python
import datetime


print(str(1.1 + 2.2))
print(repr(1.1 + 2.2))
n = datetime.datetime.now()
print(str(n))
print(repr(n))
```

    3.3000000000000003
    3.3000000000000003
    2022-12-08 09:40:31.561629
    datetime.datetime(2022, 12, 8, 9, 40, 31, 561629)
    

### 整数与不同进制的字符串的转换


```python
print("255转换为十六进制：", hex(255))
print("255转换为八进制：", oct(255))
print("255转换为二进制：", bin(255))
print("使用int将字符串转换为整数：int('23') = ", int('23'))
# 还可以指定按照多少进制来进行转换，最后返回十进制表达的整数
print("FF按照16进制来转换：", int('FF', 16))
print("377按照8进制来转换：", int('377', 8))
print("1111按照2进制来转换：", int('1111', 2))
print("使用float将字符串转换为浮点数：float(3.5) = ", float(3.5))

```

    255转换为十六进制： 0xff
    255转换为八进制： 0o377
    255转换为二进制： 0b11111111
    使用int将字符串转换为整数：int('23') =  23
    FF按照16进制来转换： 255
    377按照8进制来转换： 255
    1111按照2进制来转换： 15
    使用float将字符串转换为浮点数：float(3.5) =  3.5
    

### 格式化字符串

**Python**用字符串的`format()`方法来格式化字符串。

具体用法如下，字符串中花括号 `{}` 的部分会被format传入的参数替代，传入的值可以是字符串，也可以是数字或者别的对象。


```python
'{} {} {}'.format('a', 'b', 'c')
```




    'a b c'



可以用数字指定传入参数的相对位置：


```python
'{2} {1} {0}'.format('a', 'b', 'c')
```




    'c b a'



还可以指定传入参数的名称：


```python
'{color} {n} {x}'.format(n=10, x=1.5, color='blue')
```




    'blue 10 1.5'



可以在一起混用：


```python
'{color} {0} {x} {1}'.format(10, 'foo', x = 1.5, color='blue')
```




    'blue 10 1.5 foo'



可以用`{<field name>:<format>}`指定格式：


```python
from math import pi

# 输出域为10
'{0:10} {1:10d} {2:10.2f}'.format('foo', 5, 2 * pi)

```




    'foo                 5       6.28'



也可以使用旧式的 % 方法进行格式化：


```python
s = "some numbers:"
x = 1.34
y = 2
# 用百分号隔开，括号括起来
t = "%s  %f, %d" % (s, x, y)
t
```




    'some numbers:  1.340000, 2'



## 四、索引和分片

### 索引

对于一个有序序列，可以通过索引的方法来访问对应位置的值。字符串便是一个有序序列的例子，**Python**使用 `[]` 来对有序序列进行索引。

Python中索引是从 0 开始的，所以索引 0 对应与序列的第 1 个元素。为了得到第 5 个元素，需要使用索引值 4 。

除了正向索引，Python还引入了负索引值的用法，即从后向前开始计数，例如，索引 -2 表示倒数第 2 个元素。

**索引不能大于字符串长度**。


```python
s = "hello world"
print("s中的第一个元素: ", s[0])
print("s中的第五个元素: ", s[4])
print("s中的倒数第一个元素: ", s[-1])
```

    s中的第一个元素:  h
    s中的第五个元素:  o
    s中的倒数第一个元素:  d
    

### 分片

分片用来从序列中提取出想要的子序列，其用法为：

`var[lower:upper:step] `

+ 其范围包括 `lower` ，但不包括 `upper` ，即 `[lower, upper)`， `step` 表示取值间隔大小，如果没有默认为`1`。


```python
s = "yjqxjtu"
print(s, "中第二个到第四个元素（不包含）的切片：", s[1:3])
# 使用负索引
print(s, "中第二个到倒数第二个元素（不包含）的切片：", s[1:-2])
# lower和upper可以省略，省略lower意味着从开头开始分片
# 省略upper意味着一直分片到结尾。
print(s, "中从开头到倒数第一个元素（不包含）的切片：", s[:-1])
print(s, "中从第二个元素到结尾的切片：", s[1:])
print(s, "全部元素的切片：", s[:])
print(s, "每隔两个取一个值的切片：",s[::2])
# 当给定的upper超出字符串的长度（
# 注意：因为不包含upper，所以可以等于）时
# Python并不会报错，不过只会计算到结尾。
print(s, "超出字符串长度时的切片：", s[:100])
```

    yjqxjtu 中第二个到第四个元素（不包含）的切片： jq
    yjqxjtu 中第二个到倒数第二个元素（不包含）的切片： jqxj
    yjqxjtu 中从开头到倒数第一个元素（不包含）的切片： yjqxjt
    yjqxjtu 中从第二个元素到结尾的切片： jqxjtu
    yjqxjtu 全部元素的切片： yjqxjtu
    yjqxjtu 每隔两个取一个值的切片： yqju
    yjqxjtu 超出字符串长度时的切片： yjqxjtu
    

## 五、列表

在**Python**中，列表是一个有序的序列。

列表用一对 `[]` 生成，中间的元素用 `,` 隔开，其中的元素不需要是同一类型，同时列表的长度也不固定。


```python
l = [1, 2.0, 'hello']
print (l)
```

    [1, 2.0, 'hello']
    

空列表可以用 `[]` 或者 `list()` 生成：


```python
empty_list = []
empty_list
```




    []




```python
empty_list = list()
empty_list
```




    []



### 列表操作


```python
l1 = [1, 2.0, 'hello']
l2 = [1, 3.0, 'python']
print("要操作的列表为：l1 =  ", l1)
print("要操作的列表为：l2 =  ", l2)
print("列表长度：l1 = ",len(l1))
print("列表长度：l2 = ",len(l2))
print("列表相加：l1 + l2 = ", l1 + l2)
# 列表与整数相乘，相当于将列表重复相加：
print("l1 * 2 = ",l1 * 2)
```

    要操作的列表为：l1 =   [1, 2.0, 'hello']
    要操作的列表为：l2 =   [1, 3.0, 'python']
    列表长度：l1 =  3
    列表长度：l2 =  3
    列表相加：l1 + l2 =  [1, 2.0, 'hello', 1, 3.0, 'python']
    l1 * 2 =  [1, 2.0, 'hello', 1, 2.0, 'hello']
    

### 列表方法

- `l.count(ob)` 返回列表中元素 `ob` 出现的次数。
- `l.index(ob)` 返回列表中元素 `ob` 第一次出现的索引位置，如果 `ob` 不在 `l` 中会报错。
- `l.append(ob)` 将元素 `ob` 添加到列表 `l` 的最后。
- `l.extend(lst)` 将序列 `lst` 的元素依次添加到列表 `l` 的最后，作用相当于 `l += lst`。
- `l.insert(idx, ob)` 在索引 `idx` 处插入 `ob` ，之后的元素依次后移。
- `l.remove(ob)` 会将列表中第一个出现的 `ob` 删除，如果 `ob` 不在 `l` 中会报错。
- `l.pop(idx)` 会将索引 `idx` 处的元素删除，并返回这个元素。
- `l.sort()` 会将列表中的元素按照一定的规则排序。如果不想改变原来列表中的值，可以使用 `sorted` 函数。
- `l.reverse()` 会将列表中的元素从后向前排列。

#### 列表中某个元素个数count

`l.count(ob)` 返回列表中元素 `ob` 出现的次数。


```python
a = [11, 12, 13, 12, 11]
a.count(11)
```




    2



#### 列表中某个元素位置index

`l.index(ob)` 返回列表中元素 `ob` 第一次出现的索引位置，如果 `ob` 不在 `l` 中会报错。


```python
a.index(12)
```




    1



#### 向列表中添加单个元素

`l.append(ob)` 将元素 `ob` 添加到列表 `l` 的最后。


```python
a = [10, 11, 12]
a.append(11)
print(a)
```

    [10, 11, 12, 11]
    

append每次只添加一个元素，并不会因为这个元素是序列而将其展开：


```python
a.append([11, 12])
print (a)
```

    [10, 11, 12, 11, [11, 12]]
    

#### 向列表添加序列

`l.extend(lst)` 将序列 `lst` 的元素依次添加到列表 `l` 的最后，作用相当于 `l += lst`。


```python
a = [10, 11, 12, 11]
a.extend([1, 2])
print (a)
```

    [10, 11, 12, 11, 1, 2]
    

#### 插入元素

`l.insert(idx, ob)` 在索引 `idx` 处插入 `ob` ，之后的元素依次后移。


```python
a = [10, 11, 12, 13, 11]
# 在索引 3 插入 'a'
a.insert(3, 'a')
print (a)
```

    [10, 11, 12, 'a', 13, 11]
    

#### 移除元素

`l.remove(ob)` 会将列表中第一个出现的 `ob` 删除，如果 `ob` 不在 `l` 中会报错。


```python
a = [10, 11, 12, 13, 11]
# 移除了第一个 11
a.remove(11)
print (a)
```

    [10, 12, 13, 11]
    

#### 弹出元素

`l.pop(idx)` 会将索引 `idx` 处的元素删除，并返回这个元素。


```python
a = [10, 11, 12, 13, 11]
a.pop(2)
```




    12



#### 排序

`l.sort()` 会将列表中的元素按照一定的规则排序。


```python
a = [10, 1, 11, 13, 11, 2]
a.sort()
print (a)
```

    [1, 2, 10, 11, 11, 13]
    

如果不想改变原来列表中的值，可以使用 sorted 函数：


```python
a = [10, 1, 11, 13, 11, 2]
b = sorted(a)
print (a)
print (b)
```

    [10, 1, 11, 13, 11, 2]
    [1, 2, 10, 11, 11, 13]
    

#### 列表反向

`l.reverse()` 会将列表中的元素从后向前排列。


```python
a = [1, 2, 3, 4, 5, 6]
a.reverse()
print (a)
```

    [6, 5, 4, 3, 2, 1]
    

如果不想改变原来列表中的值，可以使用这样的方法.


```python
a = [1, 2, 3, 4, 5, 6]
b = a[::-1]
print (a)
print (b)
```

    [1, 2, 3, 4, 5, 6]
    [6, 5, 4, 3, 2, 1]
    


```python
# 如果不清楚用法，可以查看帮助
a.sort?
```

    [1;31mSignature:[0m [0ma[0m[1;33m.[0m[0msort[0m[1;33m([0m[1;33m*[0m[1;33m,[0m [0mkey[0m[1;33m=[0m[1;32mNone[0m[1;33m,[0m [0mreverse[0m[1;33m=[0m[1;32mFalse[0m[1;33m)[0m[1;33m[0m[1;33m[0m[0m
    [1;31mDocstring:[0m
    Sort the list in ascending order and return None.
    
    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).
    
    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.
    
    The reverse flag can be set to sort in descending order.
    [1;31mType:[0m      builtin_function_or_method
    

### 索引和分片

列表和字符串一样可以通过索引和分片来查看它的元素。

与字符串不同的是，**列表可以通过索引和分片来修改**。

对于字符串，如果我们通过索引或者分片来修改，Python会报错：


```python
l = [1, 2.0, 'hello']
print("修改前：", l)
l[0] = 520
print("修改后：", l)
```

    修改前： [1, 2.0, 'hello']
    修改后： [520, 2.0, 'hello']
    


```python
s = "hello world"
# 把开头的 h 改成大写
s[0] = 'H'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In [139], line 3
          1 s = "hello world"
          2 # 把开头的 h 改成大写
    ----> 3 s[0] = 'H'
    

    TypeError: 'str' object does not support item assignment


对于连续的分片（即步长为 `1` ），**Python**采用的是整段替换的方法，两者的元素个数并不需要相同，例如，将 `[11,12]` 替换为 `[1,2,3,4]`：


```python
a = [10, 11, 12, 13, 14]
a[1:3] = [1, 2, 3, 4]
print(a)
```

    [10, 1, 2, 3, 4, 13, 14]
    

这意味着，可以用这种方法来删除列表中一个连续的分片：


```python
a = [10, 1, 2, 11, 12]
print(a[1:3])
a[1:3] = []
print(a)
```

    [1, 2]
    [10, 11, 12]
    

对于不连续（间隔step不为1）的片段进行修改时，两者的元素数目必须一致, 否则会报错：


```python
a = [10, 11, 12, 13, 14]
a[::2] = [1, 2, 3]
a
```




    [1, 11, 2, 13, 3]



### 删除元素

Python提供了删除列表中元素的方法 `del`。


```python
a = [1002, 'a', 'b', 'c']
print("操作的列表：", a)
del a[0]
print("删除第一个元素后：", a)
a = [1002, 'a', 'b', 'c']
del a[1:]
print("删除第2到最后一个元素：", a)
a = [1002, 'a', 'b', 'c']
del a[::2]
print("删除间隔的元素后：", a)
```

    操作的列表： [1002, 'a', 'b', 'c']
    删除第一个元素后： ['a', 'b', 'c']
    删除第2到最后一个元素： [1002]
    删除间隔的元素后： ['a', 'c']
    

### 测试从属关系

用 `in` 来看某个元素是否在某个序列（不仅仅是列表）中，用not in来判断是否不在某个序列中。


```python
a = [10, 11, 12, 13, 14]
print(10 in a)
print(10 not in a)
```

    True
    False
    

也可以作用于字符串：


```python
s = 'hello world'
print('he' in s)
print('world' not in s)
```

    True
    False
    

列表中可以包含各种对象，甚至可以包含列表：


```python
a = [10, 'eleven', [12, 13]]
a[2]
```




    [12, 13]



## 六、可变和不可变类型

- 列表是可变的(Mutable)
- 字符串是不可变的(Immutable)

字符串方法只是返回一个新字符串，并不改变原来的值，如果想改变字符串的值，可以用重新赋值的方法。


```python
s = "hello world"
s = s.replace('world', 'Mars')
print (s)
```

    hello Mars
    

Python的六大数据类型：

1. 数字（Number)
2. 字符串(String)
3. 元组(Tuple)
4. 列表(List)
5. 集合(Set)
6. 字典(Dictionary)

Python的可变和不可变数据类型：

+ 可变的：列表、集合、字典（可以进行更改，并且更改后物理地址不会发生改变）

+ 不可变的：数字、字符串、元组（不可以进行更改，更改后就是一个新的对象了，物理地址发生了变化）

### 字符串不可变的原因

其一，列表可以通过以下的方法改变，而字符串不支持这样的变化。


```python
a = [1, 2, 3, 4]
b = a
```

此时， a 和 b 指向同一块区域，改变 b 的值， a 也会同时改变：


```python
b[0] = 100
a
```




    [100, 2, 3, 4]



其二，是字符串与整数浮点数一样被认为是基本类型，而基本类型在Python中是不可变的。

## 七、元组

### 基本操作

旧式字符串格式化中参数要用元组；在字典中当作键值；数据库的返回值......

与列表相似，元组`Tuple`也是个有序序列，但是元组是不可变的，用`()`生成。


```python
t = (10, 11, 12, 13, 14)
print("元组：",type(t))
print("操作的元组：", t)
print("元组索引：第一个元素 = ",t[0])
print("元组切片：第一个元素到第三个元素 = ",t[0:3])
```

    元组： <class 'tuple'>
    操作的元组： (10, 11, 12, 13, 14)
    元组索引：第一个元素 =  10
    元组切片：第一个元素到第三个元素 =  (10, 11, 12)
    


```python
# 元组不可变，改了会报错
t[0] = 1
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In [181], line 2
          1 # 元组不可变，改了会报错
    ----> 2 t[0] = 1
    

    TypeError: 'tuple' object does not support item assignment


### 单个元素的元组生成

由于`()`在表达式中被应用，只含有单个元素的元组容易和表达式混淆，所以采用下列方式定义只有一个元素的元组


```python
a = (10, )
print(a)
print(type(a))
```

    (10,)
    <class 'tuple'>
    


```python
a = (10)
print(type(a))
```

    <class 'int'>
    

将列表转换为元组：


```python
a = [10, 11, 12, 13, 14]
tuple(a)
```




    (10, 11, 12, 13, 14)



### 元组方法

由于元组是不可变的，所以只能有一些不可变的方法，例如计算元素个数 `count` 和元素位置 `index` ，用法与列表一样。


```python
print(a.count(10))
print(a.index(12))
```

    1
    2
    

## 八、列表与元组的速度比较

元组的生成速度会比列表快很多，迭代速度快一点，索引速度差不多。

### 生成速度


```python
print("列表生成速度：")
%timeit [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

```

    列表生成速度：
    68.1 ns ± 1.73 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
    


```python
print("元组生成速度：")
%timeit (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)

```

    元组生成速度：
    6.79 ns ± 0.135 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)
    

可以看到，元组的生成速度要比列表的生成速度快得多，相差大概一个数量级。

### 遍历速度


```python
# 产生内容相同的随机列表和元组
from numpy.random import rand
# 10000 x 4
values = rand(10000,4)

lst = [list(row) for row in values]
tup = tuple(tuple(row) for row in values)

```


```python
print("列表遍历速度：")
%timeit for row in lst: list(row)
```

    列表遍历速度：
    786 µs ± 49 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    


```python
print("元组遍历速度：")
%timeit for row in tup: tuple(row)
```

    元组遍历速度：
    352 µs ± 10.1 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    

在遍历上，元组和列表的速度表现差不多。

### 索引速度


```python
print("列表索引速度：")
%timeit for row in lst: a = row[0] + 1
```

    列表索引速度：
    2.37 ms ± 127 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    


```python
print("元组索引速度：")
%timeit for row in tup: a = row[0] + 1
```

    元组索引速度：
    2.22 ms ± 78.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    

索引速度差不多。

## 九、字典

字典 `dictionary` ，在一些编程语言中也称为 `hash` ， `map` ，是一种由键值对组成的数据结构。

顾名思义，我们把键想象成字典中的单词，值想象成词对应的定义，那么
一个词可以对应一个或者多个定义，但是这些定义只能通过这个词来进行查询。

### 基本操作

#### 空字典

**Python** 使用 `{}` 或者 `dict()` 来创建一个空的字典：


```python
a = {}
b = dict()
print("字典类型：",type(a))
print("字典类型：",type(b))
```

    字典类型： <class 'dict'>
    字典类型： <class 'dict'>
    

有了dict之后，可以用索引键值的方法向其中添加元素，也可以通过索引来查看元素的值。

#### 插入键值


```python
a["one"] = "this is number 1"
a["two"] = "this is number 2"
a
```




    {'one': 'this is number 1', 'two': 'this is number 2'}



#### 查看键值


```python
a['one']
```




    'this is number 1'



#### 更新键值


```python
a['one'] = 'yjq'
a
```




    {'one': 'yjq', 'two': 'this is number 2'}



#### 初始化字典

可以看到，Python使用`key: value`这样的结构来表示字典中的元素结构，事实上，可以直接使用这样的结构来初始化一个字典：


```python
b = {'one': 'this is number 1', 'two': 'this is number 2'}
b['one']
```




    'this is number 1'



#### 字典具有无序性

 `print` 一个字典时，**Python**并不一定按照插入键值的先后顺序进行显示,因为字典中的键本身不一定是有序的。因此，Python中不能用支持用数字索引按顺序查看字典中的值，而且数字本身也有可能成为键值，这样会引起混淆。


```python
# 会报错
a[0]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In [221], line 2
          1 # 会报错
    ----> 2 a[0]
    

    KeyError: 0


#### 键必须是不可变的类型

出于hash的目的，Python中要求这些键值对的**键**必须是**不可变**的，而值可以是任意的Python对象。

一个表示近义词的字典：


```python
synonyms = {}
synonyms['mutable'] = ['changeable', 'variable', 'varying', 'fluctuating',
                       'shifting', 'inconsistent', 'unpredictable', 'inconstant',
                       'fickle', 'uneven', 'unstable', 'protean']
synonyms['immutable'] = ['fixed', 'set', 'rigid', 'inflexible', 
                         'permanent', 'established', 'carved in stone']
synonyms
```




    {'mutable': ['changeable',
      'variable',
      'varying',
      'fluctuating',
      'shifting',
      'inconsistent',
      'unpredictable',
      'inconstant',
      'fickle',
      'uneven',
      'unstable',
      'protean'],
     'immutable': ['fixed',
      'set',
      'rigid',
      'inflexible',
      'permanent',
      'established',
      'carved in stone']}



键（或者值）的数据类型可以不同


```python
people = [
    {'first': 'Sam', 'last': 'Malone', 'name': 35},
    {'first': 'Woody', 'last': 'Boyd', 'name': 21},
    {'first': 'Norm', 'last': 'Peterson', 'name': 34},
    {'first': 'Diane', 'last': 'Chambers', 'name': 33}
]
people
```




    [{'first': 'Sam', 'last': 'Malone', 'name': 35},
     {'first': 'Woody', 'last': 'Boyd', 'name': 21},
     {'first': 'Norm', 'last': 'Peterson', 'name': 34},
     {'first': 'Diane', 'last': 'Chambers', 'name': 33}]



#### 使用dict初始化字典

除了通常的定义方式，还可以通过 `dict()` 转化来生成字典：


```python
inventory = dict(
    [('foozelator', 123),
     ('frombicator', 18), 
     ('spatzleblock', 34), 
     ('snitzelhogen', 23)
    ])
inventory
```




    {'foozelator': 123, 'frombicator': 18, 'spatzleblock': 34, 'snitzelhogen': 23}




```python
# 利用索引直接更新键值对
inventory['frombicator'] += 1
inventory
```




    {'foozelator': 123, 'frombicator': 19, 'spatzleblock': 34, 'snitzelhogen': 23}



#### 适合做键的类型

在不可变类型中，整数和字符串是字典中最常用的类型；而浮点数通常不推荐用来做键，由于浮点数的精度会引发问题：


```python
data = {}
data[1.1 + 2.2] = 6.6
# 会报错
data[3.3]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In [226], line 4
          2 data[1.1 + 2.2] = 6.6
          3 # 会报错
    ----> 4 data[3.3]
    

    KeyError: 3.3


有时候，也可以使用元组作为键值，例如，可以用元组做键来表示从第一个城市飞往第二个城市航班数的多少：


```python
connections = {}
connections[('New York', 'Seattle')] = 100
connections[('Austin', 'New York')] = 200
connections[('New York', 'Austin')] = 400
```

### 字典操作

#### get方法

之前已经见过，用索引可以找到一个键对应的值，但是当字典中没有这个键的时候，Python会报错，这时候可以使用字典的 get 方法来处理这种情况，其用法如下：

`d.get(key, default = None)`:
+ 返回字典中键 `key` 对应的值，如果没有这个键，返回 `default` 指定的值（默认是 `None` ）


```python
a = {}
a["one"] = "this is number 1"
a["two"] = "this is number 2"
print(a.get('three'))
print(a.get('three','undefined'))
```

    None
    undefined
    

#### pop方法删除元素


`pop` 方法可以用来弹出字典中某个键对应的值，同时也可以指定默认参数。

`d.pop(key, default = None)`
+ 删除并返回字典中键 key 对应的值，如果没有这个键，返回 default 指定的值（默认是 None ）。


```python
a = {}
a["one"] = "this is number 1"
a["two"] = "this is number 2"
print(a)
print(a.pop('two'))
print(a)
print("弹出不存在的键值：",a.pop('two','not exist'))
```

    {'one': 'this is number 1', 'two': 'this is number 2'}
    this is number 2
    {'one': 'this is number 1'}
    弹出不存在的键值： not exist
    

与列表一样，`del` 函数可以用来删除字典中特定的键值对，例如：


```python
del a["one"]
a
```




    {}



#### update方法更新字典

之前已经知道，可以通过索引来插入、修改单个键值对，但是如果想对多个键值对进行操作，这种方法就显得比较麻烦，好在有 `update` 方法：

`d.update(newd)`:
+ 将字典newd中的内容更新到d中去


```python
person = {}
person['first'] = "Jmes"
person['last'] = "Maxwell"
person['born'] = 1831
print(person)
# 把'first'改成'James'，同时插入'middle'的值'Clerk'：
person_modifications = {'first': 'James', 'middle': 'Clerk'}
person.update(person_modifications)
print(person)
```

    {'first': 'Jmes', 'last': 'Maxwell', 'born': 1831}
    {'first': 'James', 'last': 'Maxwell', 'born': 1831, 'middle': 'Clerk'}
    

#### in查询字典中是否有该键


```python
barn = {'cows': 1, 'dogs': 5, 'cats': 3}
print("\'chickens\' in barn ?", 'chickens' in barn)
print("\'cows\' in barn ?", 'cows' in barn)
```

    'chickens' in barn ? False
    'cows' in barn ? True
    

#### keys 方法，values 方法和items 方法

`d.keys()` :
+ 返回一个由所有键组成的列表；

`d.values()` :
+ 返回一个由所有值组成的列表；

`d.items()` :
+ 返回一个由所有键值对元组组成的列表；


```python
print("所有的键：",barn.keys())
print("键对应的值：",barn.values())
print("所有的键值对：",barn.items())
```

    所有的键： dict_keys(['cows', 'dogs', 'cats'])
    键对应的值： dict_values([1, 5, 3])
    所有的键值对： dict_items([('cows', 1), ('dogs', 5), ('cats', 3)])
    

## 十、集合

因为集合是无序的，所以当集合中存在两个同样的元素的时候，Python只会保存其中的一个（唯一性）；同时为了确保其中不包含同样的元素，集合中放入的元素只能是不可变的对象（确定性）。

### 生成集合

可以用`set()`函数来显示的生成空集合：


```python
a = set()
type(a)
```




    set



也可以使用一个列表来初始化一个集合


```python
a = set([1, 2, 3, 1])
a
```




    {1, 2, 3}



可以看到，集合中的元素是用大括号`{}`包含起来的，这意味着可以用`{}`的形式来创建集合：


```python
a = {1, 2, 3, 1}
a
```




    {1, 2, 3}



但是创建空集合的时候只能用`set`来创建，因为在Python中`{}`创建的是一个空的字典。

### 集合操作


```python
# 待操作的集合
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

#### 并

两个集合的并，返回包含两个集合所有元素的集合（去除重复）。

可以用方法 `a.union(b)` 或者操作 `a | b` 实现。


```python
print("a并b：", a.union(b))
print("b并a：", b.union(a))
print("a|b ：", a | b)

```

    a并b： {1, 2, 3, 4, 5, 6}
    b并a： {1, 2, 3, 4, 5, 6}
    a|b ： {1, 2, 3, 4, 5, 6}
    

#### 交

两个集合的交，返回包含两个集合共有元素的集合。

可以用方法 `a.intersection(b)` 或者操作 `a & b` 实现。


```python
print("a交b：", a.intersection(b))
print("b交a：", b.intersection(a))
print("a&b ：", a & b)

```

    a交b： {3, 4}
    b交a： {3, 4}
    a&b ： {3, 4}
    

#### 差

`a` 和 `b` 的差集，返回只在 `a` 不在 `b` 的元素组成的集合。

可以用方法 `a.difference(b)` 或者操作 `a - b` 实现。


```python
print("a与b的差集：", a.difference(b))
print("b与a的差集：", b.difference(a))
print("a - b：", a - b)
```

    a与b的差集： {1, 2}
    b与a的差集： {5, 6}
    a - b： {1, 2}
    

#### 对称差

`a` 和`b` 的对称差集，返回在 `a` 或在 `b` 中，但是不同时在 `a` 和 `b` 中的元素组成的集合。

可以用方法 `a.symmetric_difference(b)` 或者操作 `a ^ b` 实现（异或操作符）


```python
print("a与b的对称差集：", a.symmetric_difference(b))
print("b与a的对称差集：", b.symmetric_difference(a))
print("a ^ b：", a ^ b)
```

    a与b的对称差集： {1, 2, 5, 6}
    b与a的对称差集： {1, 2, 5, 6}
    a ^ b： {1, 2, 5, 6}
    

#### 包含关系

假设现在有这样两个集合：


```python
a = {1, 2, 3}
b = {1, 2}

```

要判断 b 是不是 a 的子集，可以用 `b.issubset(a)` 方法，或者更简单的用操作 `b <= a` ：


```python
print(b.issubset(a))
print(b<=a)
```

    True
    True
    

之对应，也可以用 `a.issuperset(b)` 或者 `a >= b` 来判断


```python
print(a.issuperset(b))
print(a>=b)
```

    True
    True
    

方法只能用来测试子集，但是操作符可以用来判断真子集


```python
print("自己是自己的子集：a <= a ", a <= a)
print("自己不是自己的真子集：a < a ", a < a)
```

    自己是自己的子集：a <= a  True
    自己不是自己的真子集：a < a  False
    

### 集合方法

#### add 方法向集合添加单个元素
跟列表的 `append` 方法类似，用来向集合添加单个元素。

`s.add(a)`:
+ 将元素 `a` 加入集合 `s` 中。


```python
t = {1, 2, 3}
t.add(5)
t
```




    {1, 2, 3, 5}



如果添加的是已有元素，集合不改变


```python
t.add(3)
t
```




    {1, 2, 3, 5}



#### update 方法向集合添加多个元素

跟列表的`extend`方法类似，用来向集合添加多个元素。

`s.update(seq)`:
+ 将seq中的元素添加到s中。


```python
t.update({5, 6, 7})
t
```




    {1, 2, 3, 5, 6, 7}



#### remove 方法移除单个元素

`s.remove(ob) `:
+ 从集合s中移除元素ob，如果不存在会报错。


```python
t.remove(1)
t
```




    {2, 3, 5, 6, 7}




```python
# 不存在会报错
t.remove(8)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In [275], line 2
          1 # 不存在会报错
    ----> 2 t.remove(8)
    

    KeyError: 8


#### pop方法弹出元素

由于集合没有顺序，不能像列表一样按照位置弹出元素，所以pop 方法删除并返回集合中任意一个元素，如果集合中没有元素会报错。


```python
t = {1, 2, 3}
print(t.pop())
print(t)
```

    1
    {2, 3}
    

#### discard方法

作用与 `remove` 一样，但是当元素在集合中不存在的时候不会报错。


```python
print(t.discard(3))
print(t)
# 不存在的元素不会报错
t.discard(29)
```

    None
    {2}
    

#### difference_update方法

`a.difference_update(b) `:
+ 从a中去除所有属于b的元素。

### 不可变集合

对应于元组（`tuple`）与列表（`list`）的关系，对于集合（`set`），**Python**提供了一种叫做不可变集合（`frozen set`）的数据结构。

使用 `frozenset` 来进行创建：


```python
s = frozenset([1, 2, 3, 'a', 1])
s
```




    frozenset({1, 2, 3, 'a'})



与集合不同的是，不可变集合一旦创建就不可以改变。

不可变集合的一个主要应用是用来**作为字典的键**，例如用一个字典来记录两个城市之间的距离：


```python
flight_distance = {}
city_pair = frozenset(['Los Angeles', 'New York'])
flight_distance[city_pair] = 2498
flight_distance[frozenset(['Austin', 'Los Angeles'])] = 1233
flight_distance[frozenset(['Austin', 'New York'])] = 1515
flight_distance
```




    {frozenset({'Los Angeles', 'New York'}): 2498,
     frozenset({'Austin', 'Los Angeles'}): 1233,
     frozenset({'Austin', 'New York'}): 1515}



由于集合不分顺序，所以不同顺序不会影响查阅结果


```python
print("The distance between New York and Austin: ",
      flight_distance[frozenset(['New York', 'Austin'])])
print("The distance between Austin and New York: ",
      flight_distance[frozenset(['Austin', 'New York'])])

```

    The distance between New York and Austin:  1515
    The distance between Austin and New York:  1515
    

## 十一、Python赋值机制


```python
x = [1, 2, 3]
y = x
x[1] = 100
print (y)
```

    [1, 100, 3]
    

上述例子中，改变变量`x`的值，变量`y`的值也随着改变，这与**Python**内部的赋值机制有关。

### 简单类型

先看如下代码在python中的执行过程:


```python
x = 500
y = x
y = 'foo'
```

**Python**分配了一个 `PyInt` 大小的内存 `pos1` 用来储存对象 `500` ，然后，Python在命名空间中让变量 `x` 指向了这一块内存，注意，整数是不可变类型，所以这块内存的内容是不可变的。

| 内存                         | 命名空间   |
| ---------------------------- | ---------- |
| `pos1 : PyInt(500)` (不可变) | `x : pos1` |

- `y = x`

**Python**并没有使用新的内存来储存变量 `y` 的值，而是在命名空间中，让变量 `y` 与变量 `x` 指向了同一块内存空间。

| 内存                         | 命名空间   |
| ---------------------------- | ---------- |
| `pos1 : PyInt(500)` (不可变) | `x : pos1` |
| `y : pos1`                   |            |

- `y = 'foo'`

**Python**此时分配一个 `PyStr` 大小的内存 `pos2` 来储存对象 `foo` ，然后改变变量 `y` 所指的对象。

| 内存                           | 命名空间   |
| ------------------------------ | ---------- |
| `pos1 : PyInt(500)` (不可变)   |            |
| `pos2 : PyStr('foo')` (不可变) | `x : pos1` |
| `y : pos2`                     |            |

对这一过程进行验证，可以使用 `id` 函数, 返回变量的内存地址。。


```python
x = 500
print("操作：x = 500")
print("x 的内存地址为：",id(x))
y = x
print("操作：y = x")
print("y的内存地址为：", id(y))
print("x和y指向同一个事物？", x is y)
print("操作：y = \'yjq\'")
y = 'yjq'
print("y的内存地址为：", id(y))
print("x和y指向同一个事物？", x is y)
```

    操作：x = 500
    x 的内存地址为： 2605788642352
    操作：y = x
    y的内存地址为： 2605788642352
    x和y指向同一个事物？ True
    操作：y = 'yjq'
    y的内存地址为： 2605525954160
    x和y指向同一个事物？ False
    

Python会为每个出现的对象进行赋值，哪怕它们的值是一样的，例如：


```python
x = 500
print("操作：x = 500")
print("x 的内存地址为：",id(x))
y = 500
print("操作：y = 500")
print("y 的内存地址为：",id(y))
print("x和y指向同一个事物？", x is y)
```

    操作：x = 500
    x 的内存地址为： 2605788642256
    操作：y = 500
    y 的内存地址为： 2605788642864
    x和y指向同一个事物？ False
    

不过，为了提高内存利用效率，对于一些简单的对象，如一些数值较小的int对象，Python采用了重用对象内存的办法：


```python
print("重用对象内存")
x = 2
print("操作：x = 2")
print("x 的内存地址为：",id(x))
y = 2
print("操作：y = 2")
print("y 的内存地址为：",id(y))
print("x和y指向同一个事物？", x is y)
```

    重用对象内存
    操作：x = 2
    x 的内存地址为： 2605436332368
    操作：y = 2
    y 的内存地址为： 2605436332368
    x和y指向同一个事物？ True
    

### 容器类型


```python
x = [500, 501, 502]
y = x
y[1] = 600
y = [700, 800]
print("x = " , x)
print("y =", y)
```

    x =  [500, 600, 502]
    y = [700, 800]
    

Python为3个PyInt分配内存 `pos1` ， `pos2` ， `pos3` （不可变），然后为列表分配一段内存 `pos4` ，它包含3个位置，分别指向这3个内存，最后再让变量 `x` 指向这个列表。

| 内存                                     | 命名空间   |
| ---------------------------------------- | ---------- |
| `pos1 : PyInt(500)` (不可变)             |            |
| `pos2 : PyInt(501)` (不可变)             |            |
| `pos3 : PyInt(502)` (不可变)             |            |
| `pos4 : PyList(pos1, pos2, pos3)` (可变) | `x : pos4` |

- `y = x`

并没有创建新的对象，只需要将 `y` 指向 `pos4` 即可。

| 内存                                     | 命名空间   |
| ---------------------------------------- | ---------- |
| `pos1 : PyInt(500)` (不可变)             |            |
| `pos2 : PyInt(501)` (不可变)             |            |
| `pos3 : PyInt(502)` (不可变)             |            |
| `pos4 : PyList(pos1, pos2, pos3)` (可变) | `x : pos4` |
| `y : pos4`                               |            |

- `y[1] = 600`

原来 `y[1]` 这个位置指向的是 `pos2` ，由于不能修改 `pos2` 的值，所以首先为 `600` 分配新内存 `pos5` 。

再把 `y[1]` 指向的位置修改为 `pos5` 。此时，由于 `pos2` 位置的对象已经没有用了，**Python**会自动调用垃圾处理机制将它回收。

| 内存                                     | 命名空间   |
| ---------------------------------------- | ---------- |
| `pos1 : PyInt(500)` (不可变)             |            |
| `pos2 :` 垃圾回收                        |            |
| `pos3 : PyInt(502)` (不可变)             |            |
| `pos4 : PyList(pos1, pos5, pos3)` (可变) |            |
| `pos5 : PyInt(600)` (不可变)             | `x : pos4` |
| `y : pos4`                               |            |

- `y = [700, 800]`

首先创建这个列表，然后将变量 `y` 指向它。

| 内存                                     | 命名空间   |
| ---------------------------------------- | ---------- |
| `pos1 : PyInt(500)` (不可变)             |            |
| `pos3 : PyInt(502)` (不可变)             |            |
| `pos4 : PyList(pos1, pos5, pos3)` (可变) |            |
| `pos5 : PyInt(600)` (不可变)             |            |
| `pos6 : PyInt(700)` (不可变)             |            |
| `pos7 : PyInt(800)` (不可变)             |            |
| `pos8 : PyList(pos6, pos7)` (可变)       | `x : pos4` |
| `y : pos8`                               |            |

对这一过程进行验证：


```python
x = [500, 501, 502]
print("操作：x = [500, 501, 502]")
print ("x[0]的地址：", id(x[0]))
print ("x[1]的地址：", id(x[1]))
print ("x[2]的地址：", id(x[2]))
print ("x的地址：", id(x))
# 赋值，id(y) 与 id(x) 相同。
y = x
print("操作：y = x")
print("y的地址：", id(y))
print("x和y指向同一个事物？", x is y)
# 修改 y[1] ，id(y) 并不改变。
y[1] = 600
print("操作：y[1] = 600")
print("y的地址：", id(y))
print("x和y指向同一个事物？", x is y)
print("id(x[1]) 和 id(y[1]) 的值改变了")
print ("x[1]的地址：", id(x[1]))
print ("y[1]的地址：", id(y[1]))
print("更改 y 的值，id(y) 的值改变")
y = [700, 800]
print("操作：y = [700, 800]")
print ("x的地址：", id(x))
print("y的地址：", id(y))
print("x和y指向同一个事物？", x is y)
```

    操作：x = [500, 501, 502]
    x[0]的地址： 2605787795568
    x[1]的地址： 2605787795504
    x[2]的地址： 2605522992784
    x的地址： 2605528612992
    操作：y = x
    y的地址： 2605528612992
    x和y指向同一个事物？ True
    操作：y[1] = 600
    y的地址： 2605528612992
    x和y指向同一个事物？ True
    id(x[1]) 和 id(y[1]) 的值改变了
    x[1]的地址： 2605522992208
    y[1]的地址： 2605522992208
    更改 y 的值，id(y) 的值改变
    操作：y = [700, 800]
    x的地址： 2605528612992
    y的地址： 2605528299712
    x和y指向同一个事物？ False
    

## 十二、判断语句

### 基本用法

判断，基于一定的条件，决定是否要执行特定的一段代码，例如判断一个数是不是正数：


```python
x = 0.5
if x > 0:
    print("Hi")
    print("x is positive")
```

    x is negative
    x is positive
    

这里，如果 `x > 0` 为 `False` ，那么程序将不会执行两条 `print` 语句。

虽然都是用 `if` 关键词定义判断，但与**C，Java**等语言不同，**Python**不使用 `{}` 将 `if` 语句控制的区域包含起来。**Python**使用的是缩进方法。同时，也不需要用 `()` 将判断条件括起来。

上面例子中的这两条语句：
```python
print("Hi")
print("x is positive")
```
就叫做一个代码块，同一个代码块使用同样的缩进值，它们组成了这条 `if` 语句的主体。

不同的缩进值表示不同的代码块，例如：

`x > 0` 时：


```python
x = 0.5
if x > 0:
    print("Hey!")
    print("x is positive")
    print("This is still part of the block")
print("This isn't part of the block, and will always print.")

```

    Hey!
    x is positive
    This is still part of the block
    This isn't part of the block, and will always print.
    

`x < 0` 时：


```python
x = -0.5
if x > 0:
    print("Hey!")
    print("x is positive")
    print("This is still part of the block")
print("This isn't part of the block, and will always print.")

```

    This isn't part of the block, and will always print.
    

在这两个例子中，最后一句并不是`if`语句中的内容，所以不管条件满不满足，它都会被执行。

一个完整的 `if` 结构通常如下所示（注意：条件后的 `:` 是必须要的，缩进值需要一样）：

一个完整的 `if` 结构通常如下所示（注意：条件后的 `:` 是必须要的，缩进值需要一样）：

```python
if <condition 1>:
    <statement 1>
    <statement 2>
elif <condition 2>: 
    <statements>
else:
    <statements> 复制ErrorOK!
```

当条件1被满足时，执行 `if` 下面的语句，当条件1不满足的时候，转到 `elif` ，看它的条件2满不满足，满足执行 `elif` 下面的语句，不满足则执行 `else` 下面的语句。

对于上面的例子进行扩展：


```python
x = 0
if x > 0:
    print ("x is positive")
elif x == 0:
    print ("x is zero")
else:
    print ("x is negative")
```

    x is zero
    

`elif` 的个数没有限制，可以是1个或者多个，也可以没有。

`else` 最多只有1个，也可以没有。

可以使用 `and` ， `or` , `not` 等关键词结合多个判断条件：


```python
x = 10
y = -5
print(x > 0 and y < 0)
print(not x > 0)
print(x < 0 or y < 0)
```

    True
    False
    True
    

这里使用这个简单的例子，假如想判断一个年份是不是闰年，按照闰年的定义，这里只需要判断这个年份是不是能被4整除，但是不能被100整除，或者正好被400整除：


```python
year = 1900
if year % 400 == 0:
    print("This is a leap year!")
# 两个条件都满足才执行
elif year % 4 == 0 and year % 100 != 0:
    print("This is a leap year!")
else:
    print("This is not a leap year.")

```

    This is not a leap year.
    

### 值的测试

**Python**不仅仅可以使用布尔型变量作为条件，它可以直接在`if`中使用任何表达式作为条件：

大部分表达式的值都会被当作`True`，但以下表达式值会被当作`False`：

- False
- None
- 0
- 空字符串，空列表，空字典，空集合


```python
mylist = [3, 1, 4, 1, 5, 9]
if mylist:
    print("The first element is:", mylist[0])
else:
    print("There is no first element.")
```

    The first element is: 3
    

修改为空列表：


```python
mylist = []
# if mylist:
if len(mylist) > 0:
    print("The first element is:", mylist[0])
else:
    print("There is no first element.")
```

    There is no first element.
    

当然这种用法并不推荐，推荐使用 `if len(mylist) > 0`: 来判断一个列表是否为空。

## 十三、循环

循环的作用在于将一段代码重复执行多次。

### while循环


```python
while <condition>:
    <statesments> 
```

**Python**会循环执行`<statesments>`，直到`<condition>`不满足为止。

例如，计算数字`0`到`1000000`的和：


```python
i = 0
total = 0
while i < 1000000:
    total += i
    i += 1
print(total)
```

    499999500000
    

之前提到，空容器会被当成 False ，因此可以用 while 循环来读取容器中的所有元素：


```python
plays = set(['Hamlet', 'Macbeth', 'King Lear'])
while plays:
    play = plays.pop()
    print('Perform', play)
```

    Perform King Lear
    Perform Hamlet
    Perform Macbeth
    

循环每次从 `plays` 中弹出一个元素，一直到 `plays` 为空为止。

### for循环

```python
for <variable> in <sequence>:
    <indented block of code> 
```
`for` 循环会遍历完`<sequence>`中所有元素为止

上一个例子可以改写成如下形式：


```python
plays = set(['Hamlet', 'Macbeth', 'King Lear'])
for play in plays:
    print('Perform', play)
```

    Perform King Lear
    Perform Hamlet
    Perform Macbeth
    

使用 `for` 循环时，注意尽量不要改变 `plays` 的值，否则可能会产生意想不到的结果。

之前的求和也可以通过 `for` 循环来实现：


```python
total = 0
for i in range(100000):
    total += i
print(total)
```

    4999950000
    

 Python 3 中，`range()` 的实现方式与 `xrange()` 函数相同，所以就不存在专用的 `xrange()`。

### continue语句

遇到 `continue` 的时候，程序会返回到循环的最开始重新执行。

例如在循环中忽略一些特定的值：


```python
values = [7, 6, 4, 7, 19, 2, 1]
for i in values:
    if i % 2 != 0:
        # 忽略奇数
        continue
    print(i/2)
```

    3.0
    2.0
    1.0
    

### break 语句

遇到 break 的时候，程序会跳出循环，不管循环条件是不是满足：


```python
command_list = ['start', 
                'process', 
                'process',
                'process', 
                'stop', 
                'start', 
                'process', 
                'stop']
while command_list:
    command = command_list.pop(0)
    if command == 'stop':
        break
    print(command)
```

    start
    process
    process
    process
    

在遇到第一个 'stop' 之后，程序跳出循环。

### else语句

与 `if` 一样， `while` 和 `for` 循环后面也可以跟着 `else` 语句，不过要和`break`一起连用。

- 当循环正常结束时，循环条件不满足， `else` 被执行；
- 当循环被 `break` 结束时，循环条件仍然满足， `else` 不执行。

不执行：


```python
values = [7, 6, 4, 7, 19, 2, 1]
for x in values:
    if x <= 10:
        print('Found:', x)
        break
else:
    print('All values greater than 10')
```

    Found: 7
    

执行：


```python
values = [11, 12, 13, 100]
for x in values:
    if x <= 10:
        print('Found:', x)
        break
else:
    print ('All values greater than 10')
```

    All values greater than 10
    

## 十四、推导式

Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。

Python 支持各种数据结构的推导式：

- 列表(list)推导式
- 字典(dict)推导式
- 集合(set)推导式
- 元组(tuple)推导式

### 列表推导式

列表推导式格式为：

```python
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]

或者
  
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
```

- `out_exp_res`：列表生成元素表达式，可以是有返回值的函数。
- `for out_exp in input_list`：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
- `if condition`：条件语句，可以过滤列表中不符合条件的值。

过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：


```python
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name)>3]
new_names
```




    ['ALICE', 'JERRY', 'WENDY', 'SMITH']



计算 30 以内可以被 3 整除的整数


```python
result = [i for i in range(30) if i % 3 == 0]
result
```




    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]



### 字典推导式

字典推导基本格式：
```python
{ key_expr: value_expr for value in collection }

或

{ key_expr: value_expr for value in collection if condition }
```

使用字符串及其长度创建字典


```python
list_test = ["google", "microsoft", "amazon"]
newdicrt = {value: len(value) for value in list_test}
print(newdicrt)
```

    {'google': 6, 'microsoft': 9, 'amazon': 6}
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    

提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：


```python
# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典
print({x: x**2 for x in range(3)})
```

    {0: 0, 1: 1, 2: 4}
    

### 集合推导式

集合推导式基本格式：

```python
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
```

示例如下：



```python
# 计算数字 1,2,3 的平方数
print({i ** 2 for i in {1, 2, 3}})
# 判断不是 abc 的字母并输出
print({x for x in 'abracadabra' if x not in 'abc'})
```

    {1, 4, 9}
    {'d', 'r'}
    

### 元组推导式（生成器表达式）

元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。

元组推导式基本格式：

```python
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
```

元组推导式和列表推导式的用法也完全相同，只是元组推导式是用 **()** 圆括号将各部分括起来，而列表推导式用的是中括号 **[]**，另外元组推导式返回的结果是一个生成器对象。

> 在Python中使用了yield的函数被成为生成器（generator）
> 当一个列表中含大量元素时，如果一次性生成这些元素并保存在列表中，> 将大量的内存空间，对于这个问题，我们可以通过生成器（generator）来解决，根据需要进行计算并获取列表中某个元素的值。
> 
> 对于生成器对象，也可以向其他可迭代对象一样使用for循环遍历对象中的> 每一个元素。
>


例如，我们可以使用下面的代码生成一个包含数字 1~9 的元组：


```python
a = (x for x in range(1,10))
print(a) # <generator object <genexpr> at 0x000001D43B358510>
print(tuple(a))
```

    <generator object <genexpr> at 0x0000025EB5C94120>
    (1, 2, 3, 4, 5, 6, 7, 8, 9)
    

## 十五、函数

### 定义函数

函数`function`，通常接受输入参数，并有返回值。

它负责完成某项特定任务，而且相较于其他代码，具备相对的独立性。

```python
def add(x, y):
    """Add two numbers"""
    a = x + y
    return a
```

函数通常有一下几个特征：

- 使用 `def` 关键词来定义一个函数。
- `def` 后面是函数的名称，括号中是函数的参数，不同的参数用 `,` 隔开， `def foo():` 的形式是必须要有的，参数可以为空；
- 使用缩进来划分函数的内容；
- `docstring` 用 `"""` 包含的字符串，用来解释函数的用途，可省略；
- `return` 返回特定的值，如果省略，返回 `None` 。

### 使用函数

使用函数时，只需要将参数换成特定的值传给函数。

Python并没有限定参数的类型，因此可以使用不同的参数类型：


```python
def add(x, y):
    """Add two numbers"""
    a = x + y
    return a
```


```python
print(add(2,3))
print(add('yjq','xjtu'))
```

    5
    yjqxjtu
    

在这个例子中，如果传入的两个参数不可以相加，那么Python会将报错：


```python
print(add(2,'22'))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In [360], line 1
    ----> 1 print(add(2,'22'))
    

    Cell In [356], line 3, in add(x, y)
          1 def add(x, y):
          2     """Add two numbers"""
    ----> 3     a = x + y
          4     return a
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'


如果传入的参数数目与实际不符合，也会报错：


```python
print(add(1))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In [361], line 1
    ----> 1 print(add(1))
    

    TypeError: add() missing 1 required positional argument: 'y'


传入参数时，Python提供了两种选项，第一种是上面使用的按照位置传入参数，另一种则是使用关键词模式，显式地指定参数的值：


```python
print(add(y = 12,x = 10))
```

    22
    

可以混合这两种模式


```python
print(add(2, y = 3))
```

    5
    

### 设定参数默认值

可以在函数定义的时候给参数设定默认值，例如：


```python
def quad(x, a=1, b=0, c=0):
    return a*x**2 + b*x + c

# 可以省略有默认值的参数
print(quad(2.0))
# 可以修改参数的默认值
print(quad(2.0, b =3))
```

    4.0
    10.0
    

注意，在使用混合语法时，要注意不能给同一个值赋值多次，否则会报错，例如：


```python
print(quad(2.0, 2, a=2))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In [367], line 1
    ----> 1 print(quad(2.0, 2, a=2))
    

    TypeError: quad() got multiple values for argument 'a'


### 接收不定参数

使用如下方法，可以使函数接受不定数目的参数：


```python
def add(x, *args):
    total = x
    for arg in args:
        total += arg
    return total
```

这里，`*args` 表示参数数目不定，可以看成一个元组，把第一个参数后面的参数当作元组中的元素。


```python
print(add(1, 2, 3, 4))
print(add(1, 2))
```

    10
    3
    

这样定义的函数不能使用关键词传入参数，要使用关键词，可以这样：


```python
def add(x, **kwargs):
    total = x
    for arg, value in kwargs.items():
        print("adding ", arg)
        total += value
    return total
```

这里， `**kwargs` 表示参数数目不定，相当于一个字典，关键词和值对应于键值对。


```python
print(add(10, y=11, z=12, w=13))
```

    adding  y
    adding  z
    adding  w
    46
    

再看这个例子，可以接收任意数目的位置参数和键值对参数：


```python
def foo(*args, **kwargs):
    print(args, kwargs)

foo(2, 3, x='bar', z=10)
```

    (2, 3) {'x': 'bar', 'z': 10}
    

不过要按顺序传入参数，先传入位置参数 args ，在传入关键词参数 kwargs 。

### 返回多个值


```python
from math import atan2

def to_polar(x, y):
    r = (x**2 + y**2) ** 0.5
    theta = atan2(y, x)
    return r, theta
# Python将返回的两个值变成了元组
print(to_polar(3, 4))
```

    (5.0, 0.9272952180016122)
    

因为这个元组中有两个值，所以可以使用

```python
r, theta = to_polar(3, 4) 
```

给两个值赋值。

列表也有相似的功能：


```python
a, b, c = [1, 2, 3]
print(a, b, c)
```

    1 2 3
    

事实上，不仅仅返回值可以用元组表示，也可以将参数用元组以这种方式传入：


```python
def add(x, y):
    """Add two numbers"""
    a = x + y
    return a

z = (2, 3)
print(add(*z))
```

    5
    

事实上，还可以通过字典传入参数来执行函数：


```python
def add(x, y):
    """Add two numbers"""
    a = x + y
    return a

w = {'x': 2, 'y': 3}
print(add(**w))
```

    5
    

## 十六、模块和包

### 模块

Python会将所有 `.py` 结尾的文件认定为Python代码文件，考虑下面的脚本 `ex1.py` ：


```python
%%writefile ex1.py

PI = 3.1416

def sum(lst):
    tot = lst[0]
    for value in lst[1:]:
        tot = tot + value
    return tot

w = [0, 1, 2, 3]
print(sum(w), PI)
```

    Writing ex1.py
    

可以执行它：


```python
%run ex1.py
```

    6 3.1416
    

这个脚本可以当作一个模块，可以使用`import`关键词加载并执行它（这里要求`ex1.py`在当前工作目录）：


```python
import ex1
```


```python
ex1
```




    <module 'ex1' from 'd:\\研究生资料\\python-learning\\basic-knowledge\\ex1.py'>




```python
# 打印模块中的变量
print(ex1.PI)
# 使用模块中的函数
print(ex1.sum([2,3,4]))
```

    3.1416
    9
    

为了提高效率，**Python**只会载入模块一次，已经载入的模块再次载入时，Python并不会真正执行载入操作，哪怕模块的内容已经改变。

例如，这里重新导入 `ex1` 时，并不会执行 `ex1.py` 中的 `print` 语句：


```python
import ex1
```

需要重新导入模块时，可以使用reload强制重新载入它，例如：


```python
import importlib 
importlib.reload(ex1)
```

    6 3.1416
    




    <module 'ex1' from 'd:\\研究生资料\\python-learning\\basic-knowledge\\ex1.py'>




```python
# 删除生成的文件
import os 
os.remove('ex1.py')
```

### __name__属性

有时候我们想将一个 `.py` 文件既当作脚本，又能当作模块用，这个时候可以使用 `__name__` 这个属性。

只有当文件被当作脚本执行的时候， `__name__`的值才会是 `'__main__'`，所以我们可以：


```python
%%writefile ex2.py

PI = 3.1416

def sum(lst):
    """ Sum the values in a list
    """
    tot = 0
    for value in lst:
        tot = tot + value
    return tot

def add(x, y):
    " Add two values."
    a = x + y
    return a

def test():
    w = [0,1,2,3]
    assert(sum(w) == 6)
    print('test passed.')

if __name__ == '__main__':
    test()

```

    Overwriting ex2.py
    


```python
# 运行文件
%run ex2.py
```

    test passed.
    


```python
# 当作模块导入， `test()` 不会执行
import ex2
# 可以使用其中的变量
print(ex2.PI)
```

    3.1416
    

使用别名：


```python
import ex2 as e2
e2.PI
```




    3.1416



### 其他导入方法

可以从模块中导入变量：


```python
from ex2 import add, PI
```

使用 `from` 后，可以直接使用 `add` ， `PI`：


```python
add(2,4)
```




    6



或者使用 `*` 导入所有变量：


```python
from ex2 import *
add(3, 4.5)
```




    7.5



这种导入方法不是很提倡，因为如果你不确定导入的都有哪些，可能覆盖一些已有的函数。

删除文件：


```python
import os
os.remove('ex2.py')
```

### 包

假设我们有这样的一个文件夹：

foo/

- `__init__.py`
- `bar.py` (defines func)
- `baz.py` (defines zap)

这意味着 foo 是一个包，我们可以这样导入其中的内容：

```python
from foo.bar import func
from foo.baz import zap

```

`bar` 和 `baz` 都是 `foo` 文件夹下的 `.py` 文件。

导入包要求：

- 文件夹 `foo` 在**Python**的搜索路径中
- `__init__.py` 表示 `foo` 是一个包，它可以是个空文件。

### 常用的标准库

- re 正则表达式
- copy 复制
- math, cmath 数学
- decimal, fraction
- sqlite3 数据库
- os, os.path 文件系统
- gzip, bz2, zipfile, tarfile 压缩文件
- csv, netrc 各种文件格式
- xml
- htmllib
- ftplib, socket
- cmd 命令行
- pdb
- profile, cProfile, timeit
- collections, heapq, bisect 数据结构
- mmap
- threading, Queue 并行
- multiprocessing
- subprocess
- pickle, cPickle
- struct

## 十七、异常


```python
import math

while True:
    try:
        text = input()
        if text[0] == 'q':
            break
        x = float(text)
        y = math.log10(x)
        print ("log10({0}) = {1}".format(x, y))
    except ValueError:
        print("the value must be greater than 0")
```

    log10(100.0) = 2.0
    log10(1.0) = 0.0
    

一旦 `try` 块中的内容出现了异常，那么 `try` 块后面的内容会被忽略，**Python**会寻找 `except` 里面有没有对应的内容，如果找到，就执行对应的块，没有则抛出这个异常。

在上面的例子中，`try` 抛出的是 `ValueError`，`except` 中有对应的内容，所以这个异常被 `except` 捕捉到，程序可以继续执行：


```python
import math

while True:
    try:
        text = input()
        if text[0] == 'q':
            break
        x = float(text)
        y = math.log10(x)
        print ("log10({0}) = {1}".format(x, y))
    except ValueError:
        print("the value must be greater than 0")
```

    the value must be greater than 0
    the value must be greater than 0
    

### 捕捉不同的错误类型


```python
import math

while True:
    try:
        text = input()
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print ("log10({0}) = {1}".format(x, y))
    except ValueError:
        print ("the value must be greater than 0")
```

假设我们将这里的 y 更改为 1 / math.log10(x)，此时输入 1：


```python
import math

while True:
    try:
        text = input()
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print ("log10({0}) = {1}".format(x, y))
    except ValueError:
        print ("the value must be greater than 0")
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    Cell In [411], line 9
          7         break
          8     x = float(text)
    ----> 9     y = 1 / math.log10(x)
         10     print ("log10({0}) = {1}".format(x, y))
         11 except ValueError:
    

    ZeroDivisionError: float division by zero


因为我们的 `except` 里面并没有 `ZeroDivisionError`，所以会抛出这个异常，我们可以通过两种方式解决这个问题：

#### 捕捉所有异常

将`except` 的值改成 `Exception` 类，来捕获所有的异常。


```python
import math

while True:
    try:
        text = input()
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print ("log10({0}) = {1}".format(x, y))
    except Exception:
        print("invalid value")
```

    invalid value
    

#### 指定特定值

这里，我们把 `ZeroDivisionError` 加入 `except` 。


```python
import math

while True:
    try:
        text = input()
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print ("log10({0}) = {1}".format(x, y))
    except(ValueError, ZeroDivisionError):
        print("invalid value")
```

    invalid value
    

或者另加处理：


```python
import math

while True:
    try:
        text = input()
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print("1 / log10({0}) = {1}".format(x, y))
    except ValueError:
        print("the value must be greater than 0")
    except ZeroDivisionError:
        print("the value must not be 1")
```

    the value must be greater than 0
    the value must not be 1
    

事实上,我们还可以将这两种方式结合起来,用 Exception 来捕捉其他的错误：


```python
import math

while True:
    try:
        text = input()
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print("1 / log10({0}) = {1}".format(x, y))
    except ValueError:
        print("the value must be greater than 0")
    except ZeroDivisionError:
        print("the value must not be 1")
    except Exception:
        print("unexpected error")
```

    unexpected error
    

### 得到异常的具体信息

为了得到异常的具体信息，可以使用`sys.exc_info()`：


```python
import math
import sys

while True:
    try:
        text = input()
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print ("1 / log10({0}) = {1}".format(x, y))
    except ValueError :
        print(sys.exc_info())
    except ZeroDivisionError:
        print ("the value must not be 1")
    except Exception as exc:
        print ("unexpected error:", sys.exc_info())

```

    (<class 'ValueError'>, ValueError('math domain error'), <traceback object at 0x0000025EA58ECC00>)
    the value must not be 1
    unexpected error: (<class 'IndexError'>, IndexError('string index out of range'), <traceback object at 0x0000025EA58ECC00>)
    

### 自定义异常

异常是标准库中的类，这意味着我们可以自定义异常类


```python
class CommandError(ValueError):
    pass
```

这里我们定义了一个继承自 ValueError 的异常类，异常类一般接收一个字符串作为输入，并把这个字符串当作异常信息，例如：


```python
valid_commands = {'start', 'stop', 'pause'}

while True:
    command = input()
    if command.lower() not in valid_commands:
        raise CommandError('Invalid commmand: %s' % command)
```


    ---------------------------------------------------------------------------

    CommandError                              Traceback (most recent call last)

    Cell In [425], line 6
          4 command = input()
          5 if command.lower() not in valid_commands:
    ----> 6     raise CommandError('Invalid commmand: %s' % command)
    

    CommandError: Invalid commmand: yjq


使用 `raise` 关键词来抛出异常，可以使用 `try/except` 块来捕捉这个异常：


```python
valid_commands = {'start', 'stop', 'pause'}

while True:
    command = input()
    try:
        if command[0] == 'q':
            break
        if command.lower() not in valid_commands:
            raise CommandError('Invalid commmand: %s' % command)
    except CommandError:
        print('Bad command string: "%s"' % command)
```

    Bad command string: "yjq"
    

由于 `CommandError` 继承自 `ValueError`，也可以使用 `except ValueError` 来捕获这个异常。

### finally

`try/catch` 块还有一个可选的关键词 `finally`。

不管 `try` 块有没有异常， `finally` 块的内容总是会被执行，而且会在抛出异常前执行，因此可以用来作为安全保证，比如确保打开的文件被关闭。。


```python
try:
    print(1)
finally:
    print('finally was called.')

```

    1
    finally was called.
    


```python
# 在抛出异常前执行
try:
    print(1 / 0)
finally:
    print('finally was called.')
```

    finally was called.
    


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    Cell In [429], line 3
          1 # 在抛出异常前执行
          2 try:
    ----> 3     print(1 / 0)
          4 finally:
          5     print('finally was called.')
    

    ZeroDivisionError: division by zero


如果异常被捕获了，在最后执行


```python
try:
    print(1 / 0)
except ZeroDivisionError:
    print('divide by 0.')
finally:
    print('finally was called.')

```

    divide by 0.
    finally was called.
    

## 十八、警告

出现了一些需要让用户知道的问题，但又不想停止程序，这时候我们可以使用警告：

首先导入警告模块：


```python
import warnings
```

在需要的地方，我们使用 `warnings` 中的 `warn` 函数：

```python
warn(msg, WarningType = UserWarning)
```


```python
def month_warning(m):
    if not 1<= m <= 12:
        msg = "month (%d) is not between 1 and 12" % m
        warnings.warn(msg, RuntimeWarning)

month_warning(13)
```

    C:\Users\26969\AppData\Local\Temp\ipykernel_2204\2502358554.py:4: RuntimeWarning: month (13) is not between 1 and 12
      warnings.warn(msg, RuntimeWarning)
    

有时候我们想要忽略特定类型的警告，可以使用 `warnings` 的 `filterwarnings` 函数：

```python
filterwarnings(action, category) 
```
将 `action` 设置为 `'ignore'` 便可以忽略特定类型的警告：



```python
warnings.filterwarnings(action = 'ignore', category = RuntimeWarning)

month_warning(13)
```

## 十九、文件读写

写入测试文件：


```python
%%writefile test.txt
this is a test file.
i love xjtu
```

    Overwriting test.txt
    

### 读文件 


Python **open()** 方法用于打开一个文件，并返回文件对象。

在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 **OSError**。

**注意**: 使用 **open()** 方法一定要保证关闭文件对象，即调用 **close()** 方法。

**open()** 函数常用形式是接收两个参数：文件名(file)和模式(mode)。

```python
open(file, mode='r')
```

完整的语法格式：
```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
参数说明:

- file: 必需，文件路径（相对或者绝对路径）。
- mode: 可选，文件打开模式
- buffering: 设置缓冲
- encoding: 一般使用utf8
- errors: 报错级别
- newline: 区分换行符
- closefd: 传入的file参数类型
- opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

mode 参数有：

| 模式 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| t    | 文本模式 (默认)。                                            |
| x    | 写模式，新建一个文件，如果该文件已存在则会报错。             |
| b    | 二进制模式。                                                 |
| +    | 打开一个文件进行更新(可读可写)。                             |
| U    | 通用换行模式（**Python 3 不支持**）。                        |
| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。 |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。 |
| w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

默认为文本模式，如果要以二进制模式打开，加上 **b** 。





```python
f = open('test.txt')
# 使用 read 方法来读入文件中的所有内容：
text = f.read()
print(text)
```

    this is a test file.
    i love xjtu
    
    

也可以按照行读入内容，readlines 方法返回一个列表，每个元素代表文件中每一行的内容：


```python
f = open('test.txt')
lines = f.readlines()
print (lines)
```

    ['this is a test file.\n', 'i love xjtu\n']
    

使用完文件之后，需要将文件关闭。


```python
f.close()
```

事实上，我们可以将 f 放在一个循环中，得到它每一行的内容：


```python
f = open('test.txt')
for line in f:
    print(line)
f.close()
```

    this is a test file.
    
    i love xjtu
    
    

### 写文件

使用 open 函数的写入模式来写文件：


```python
f = open('myfile.txt', 'w')
f.write('hello world!')
f.close()
```

使用 w 模式时，如果文件不存在会被创建，我们可以查看是否真的写入成功：


```python
print(open('myfile.txt').read())
```

    hello world!
    

如果文件已经存在， w 模式会覆盖之前写的所有内容：


```python
f = open('myfile.txt', 'w')
f.write('another hello world!')
f.close()
print (open('myfile.txt').read())
```

    another hello world!
    

除了写入模式，还有追加模式 a ，追加模式不会覆盖之前已经写入的内容，而是在之后继续写入：


```python
f = open('myfile.txt', 'a')
f.write('... and more')
f.close()
print (open('myfile.txt').read())
```

    another hello world!... and more
    

写入结束之后一定要将文件关闭，否则可能出现内容没有完全写入文件中的情况。

还可以使用读写模式 w+：


```python
f = open('myfile.txt', 'w+')
f.write('hello world!')
f.seek(6)
print (f.read())
f.close()
```

    world!
    

这里 `f.seek(6)` 移动到文件的第6个字符处，然后 `f.read()` 读出剩下的内容。

### 二进制文件

二进制读写模式 b：


```python
import os
f = open('binary.bin', 'wb')
f.write(os.urandom(16))
f.close()

f = open('binary.bin', 'rb')
print (repr(f.read()))
f.close()
```

    b'\xc7\xe3.\xc9\xc2;r\x89\xa5\xb5\xb3\xae\xd9\x1c\x1ef'
    


```python
import os
os.remove('binary.bin')
```

### with方法

事实上，**Python**提供了更安全的方法，当 `with` 块的内容结束后，**Python**会自动调用它的`close` 方法，确保读写的安全：


```python
with open('newfile.txt','w') as f:
    for i in range(3000):
        x = 1.0 / (i + 1000)
        f.write('hello world: ' + str(i) + '\n')
```

与 try/exception/finally 效果相同，但更简单。
