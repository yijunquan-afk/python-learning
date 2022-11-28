"""
列表推导式
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]
或者 
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
"""
names = ["yjq", "mhy", "ywq", "zdy"]
new_names = [name for name in names if len(names) > 3]
print(new_names)

# 计算 30 以内可以被 3 整除的整数：
mul = [num for num in range(30) if num % 3 == 0]
print(mul)

"""
字典推导式
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }
"""
list_test = ["google", "microsoft", "amazon"]
newdicrt = {value: len(value) for value in list_test}
print(newdicrt)
# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典
print({x: x**2 for x in range(5)})

"""
集合推导式
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
"""
# 计算数字 1,2,3 的平方数
print({i ** 2 for i in {1, 2, 3}})
# 判断不是 abc 的字母并输出
print({x for x in 'abracadabra' if x not in 'abc'})

"""  
元组推导式（生成器表达式）
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
元组推导式和列表推导式的用法也完全相同，
只是元组推导式是用 () 圆括号将各部分括起来，
而列表推导式用的是中括号 []，
另外元组推导式返回的结果是一个生成器对象。
例如，我们可以使用下面的代码生成一个包含数字 1~9 的元组：
"""
a = (x for x in range(1,10))
print(a) # <generator object <genexpr> at 0x000001D43B358510>
print(tuple(a))