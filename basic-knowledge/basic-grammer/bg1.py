import keyword

# 输出当前python版本的关键字
print(keyword.kwlist)

"""
多行注释
"""
print("hello python")

if True:
    print("true")
else:
    print("false")

""" 
print 默认输出是换行的，
如果要实现不换行需要在变量末尾加上 end=""
"""
print(12,end="")
print(13,end="")