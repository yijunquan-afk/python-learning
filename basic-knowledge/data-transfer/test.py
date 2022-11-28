""" 
整数型和浮点型运算会隐式转为浮点型
"""
num_int = 123
num_float = 1.23
num_new = num_int+num_float
print(type(num_int))
print(type(num_float))
print(num_new)
print(type(num_new))

"""  
显式转化
"""
print(int(1.23))
print(float(1))
print(str(234))