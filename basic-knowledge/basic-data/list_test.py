list = ["abcd", 123, 456, "yjq", 20.2]
print(list)
print(list[0])
print(list[0:-1])
print(list[1:3])
# list可以修改
list[0] = "a"
print(list)
tuple = ("a", 1, 2.0)
print(tuple)
# tuple不能修改
# tuple[0]='b'

# set
set = {"yjq", "mhy", "love"}
print(set)
if "you" in set:
    print("in the set!")
else:
    print("not in the set!")
set2 = {"yjq", "love"}
print(set-set2)
print(set | set2)
print(set & set2)

# dictionary

dict = {}  # 创建空字典
dict["yjq"] = "yijunquan"
dict["mhy"] = "maihaiying"
print(dict["mhy"])
print(dict)

mydict = {
    "name": "yijunquan",
    "sex": "male"
}
print(mydict)
print(dict.keys())
print(dict.values())
