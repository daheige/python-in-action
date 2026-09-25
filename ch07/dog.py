# 类class定义
# 命名约定很有⽤：通常可以认为⾸字⺟⼤写的名
# 称（如 Dog）指的是类
class Dog:
    """一次模拟小狗的简单尝试，类的定义"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


# 根据类创建实例
# 在处理这⾏代码时，Python 调⽤
# Dog 类的 __init__() ⽅法，并传⼊实参
# __init__()
# ⽅法创建⼀个表⽰特定⼩狗的实例，并且使⽤提供的值设置属性 name 和
# age。接下来，Python 返回⼀个表⽰这条⼩狗的实例，⽽我们将这个实例赋
# 给变量 dog
dog = Dog("alex", 5)
print("dog.name:", dog.name)  #  访问属性
print("dog.age:", dog.age)
# 调用类实例上的方法
dog.sit()
dog.roll_over()

#  创建多个实例
d1 = Dog("xiaohei", 6)
d1.sit()
