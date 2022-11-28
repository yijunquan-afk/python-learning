class Employee:
    empCount = 0

    # 类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    # self 代表类的实例，self 在定义类的方法时是必须有的，
    # 虽然在调用时不必传入相应的参数
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)
emp1=Employee("yjq",1000)
emp2=Employee("mhy",2000)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
print(emp1.age)
print("Total employee ", Employee.empCount)
del emp1.age  # 删除 'age' 属性
# print(emp1.age)
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
print(hasattr(emp1, 'age'))   # 如果存在 'age' 属性返回 True。
print(getattr(emp1, 'age'))    # 返回 'age' 属性的值
delattr(emp1, 'age')    # 删除属性 'age'

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)