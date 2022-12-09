# Matplotlib入门[02]——style配置pyplot风格

> 参考：
>
> + [https://ailearning.apachecn.org/](https://ailearning.apachecn.org/)
> + [Matplotlib官网](https://matplotlib.org/)
>
> 使用Jupyter进行练习

![Logo image](https://matplotlib.org/stable/_static/images/logo2.svg)



```python
import matplotlib.pyplot as plt
import numpy as np
```

`style` 是 `pyplot` 的一个子模块，方便进行风格转换， `pyplot` 有很多的预设风格，可以使用 `plt.style.available` 来查看：


```python
plt.style.available
```




    ['Solarize_Light2',
     '_classic_test_patch',
     'bmh',
     'classic',
     'dark_background',
     'fast',
     'fivethirtyeight',
     'ggplot',
     'grayscale',
     'seaborn',
     'seaborn-bright',
     'seaborn-colorblind',
     'seaborn-dark',
     'seaborn-dark-palette',
     'seaborn-darkgrid',
     'seaborn-deep',
     'seaborn-muted',
     'seaborn-notebook',
     'seaborn-paper',
     'seaborn-pastel',
     'seaborn-poster',
     'seaborn-talk',
     'seaborn-ticks',
     'seaborn-white',
     'seaborn-whitegrid',
     'tableau-colorblind10']



默认风格


```python
x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

plt.plot(x, y)

plt.show()
```


![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02style%E9%85%8D%E7%BD%AEpylplot%E9%A3%8E%E6%A0%BC_5_0.png)
    


例如，模仿 `R` 语言中常用的 `ggplot` 风格：


```python
plt.style.use('ggplot')

plt.plot(x, y)

plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02style%E9%85%8D%E7%BD%AEpylplot%E9%A3%8E%E6%A0%BC_7_0.png)
​    


使用 context 将风格改变限制在某一个代码块内：


```python
plt.figure()
with plt.style.context(('dark_background')):
    plt.subplot(211)
    plt.plot(x, y, 'r-o')
    plt.show()
# 在代码块外绘图则仍然是全局的风格。
plt.subplot(212)
plt.plot(x, y, 'r-o')
plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02style%E9%85%8D%E7%BD%AEpylplot%E9%A3%8E%E6%A0%BC_9_0.png)
​    




![png](02style%E9%85%8D%E7%BD%AEpylplot%E9%A3%8E%E6%A0%BC_files/02style%E9%85%8D%E7%BD%AEpylplot%E9%A3%8E%E6%A0%BC_9_1.png)
    


还可以混搭使用多种风格，不过最右边的一种风格会将最左边的覆盖：


```python
plt.style.use(['dark_background', 'ggplot'])

plt.plot(x, y, 'r-o')
plt.show()
```


​    
![png](https://note-image-1307786938.cos.ap-beijing.myqcloud.com/typora/02style%E9%85%8D%E7%BD%AEpylplot%E9%A3%8E%E6%A0%BC_11_0.png)
​    

