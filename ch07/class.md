# 创建和使⽤类
根据约定，在 Python 中，⾸字⺟⼤写的名称指的是类。因为这是我们创建的
全新的类，所以定义时不加括号。然后是⼀个⽂档字符串，对这个类的功能做了描述。
```python
# 类class定义
class Dog:
    """一次模拟小狗的简单尝试，类的定义"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")
```
- __init__()是⼀个特殊⽅法，每当你根据 Dog 类创建新实例时，Python 都会⾃动运⾏它。
- 在这个⽅法的名称中，开头和末尾各有两个下划线，这是⼀种约定，旨在避免 Python 默认⽅法与普通⽅法发⽣名称冲突。务必确保 __init__() 的两边都有两个下划线，否则当你使⽤类来创建实例时，将不会⾃动调⽤这个⽅法，进⽽引发难以发现的错误。

1. 为何必须在⽅法定义中包含形参 self 呢？因为当 Python 调⽤这个⽅法来创建 Dog 实例时，将⾃动传⼊实参 self。
2. 每个与实例相关联的⽅法调⽤都会⾃动传递实参 self，该实参是⼀个指向实例本⾝的引⽤，让实例能够访问类中的属性和⽅法。
3. 当我们创建 Dog 实例时，Python 将调⽤ Dog 类的 __init__() ⽅法。我们将通过实参向 Dog() 传递名字和年龄；self 则会⾃动传递，因此不需要我们来传递。每当我们根据 Dog 类创建实例时，都只需给最后两个形参（name 和 age）提供值。
4. 在 __init__() ⽅法内定义的两个变量都有前缀 self 。以self为前缀的变量可供类中的所有⽅法使⽤，可以通过类的任意实例来访问。self.name = name 获取与形参 name 相关联的值，并将其赋给变量name，然后该变量被关联到当前创建的实例。self.age = age 的作⽤与此类似。像这样可通过实例访问的变量称为属性（attribute）

# 继承
在编写类时，并⾮总是要从头开始。如果要编写的类是⼀个既有的类的特
殊版本，可使⽤继承（inheritance）。当⼀个类继承另⼀个类时，将⾃动获
得后者的所有属性和⽅法。原有的类称为⽗类（parent class），⽽新类称为
⼦类（child class）。⼦类不仅继承了⽗类的所有属性和⽅法，还可定义⾃
⼰的属性和⽅法。

## ⼦类的 __init__() ⽅法
在既有的类的基础上编写新类，通常要调⽤⽗类的 __init__() ⽅法。这
将初始化在⽗类的 __init__() ⽅法中定义的所有属性，从⽽让⼦类也可
以使⽤这些属性。

super() 是⼀个特殊的函数，让你能够调⽤⽗类的⽅法（⻅❹）。这⾏代
码让 Python 调⽤ Car 类的 __init__() ⽅法，从⽽让 ElectricCar 实
例包含这个⽅法定义的所有属性。⽗类也称为超类（superclass），函数名
super 由此得名。
```python
# 电动车继承了Car
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 40 # 给子类添加成员，电池容量

    def run(self):
        print("electric car running...")
    def desc_battery_size(self):
        print(f"this ele car battery_size is {self.battery_size}")

ele_car = ElectricCar("ele", "a1", 2026)
ele_car.read_odometer()
ele_car.run()
```

# 组合（将实例⽤作属性）
在使⽤代码模拟实物时，你可能会发现⾃⼰给类添加了太多细节：属性和
⽅法越来越多，⽂件越来越⻓。在这种情况下，可能需要将类的⼀部分提
取出来，作为⼀个独⽴的类。将⼤型类拆分成多个协同⼯作的⼩类，这种
⽅法称为组合（composition）

```python
# 组合
# 通过定义 Battery 类，将电动车的功能属性，以组合的方式嵌入到 EleCar2 类中
class Battery:
    # 初始化类的时，成员变量也可以指定默认值
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def desc_battery_size(self):
        print(f"this ele car battery_size is {self.battery_size}")


class EleCar2(Car):
    def __init__(self, make, model, year):
        """
        每当 __init__() ⽅法被调⽤时，都将执⾏该操作，
        因此现在每个 EleCar2 实例都包含⼀个⾃动创建的 Battery 实例。
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = EleCar2("nissan", "leaf", 2025)
print(my_leaf.get_descriptive_name())
```
# 小结
在解决上述问题时，从较⾼的逻辑层⾯（⽽不是语法层⾯）思考。你考虑的不是 Python，⽽是如何使⽤代码来
表⽰实际事物。达到这种境界后，你会经常发现，对现实世界的建模⽅法
没有对错之分。

有些⽅法的效率更⾼，但要找出效率最⾼的表⽰法，需要
⼀定的实践。只要代码能够像你希望的那样运⾏，就说明你已经做得很好
了！即便发现⾃⼰不得不多次尝试使⽤不同的⽅法来重写类，也不必⽓
馁。要编写出⾼效、准确的代码，这是必经之路。

# 导⼊类
随着不断地给类添加功能，⽂件可能变得很⻓，即便妥善地使⽤了继承和
组合亦如此。遵循 Python 的整体理念，应该让⽂件尽量整洁。Python 在这
⽅⾯提供了帮助，允许你将类存储在模块中，然后在主程序中导⼊所需的
模块。

```python
# 从 car.py 模块中导入成员
from car import Car, EleCar2, ElectricCar
```

# 从一个模块中导入另一个模块
有时候，需要将类分散到多个模块中，以免模块太⼤或者在同⼀个模块中
存储不相关的类。在将类存储在多个模块中时，你可能会发现⼀个模块中
的类依赖于另⼀个模块中的类。在这种情况下，可在前⼀个模块中导⼊必
要的类。
```python
# 从一个模块中导入另一个模块
from battery import Battery
```

# 找到合适的⼯作流程
如你所⻅，在组织⼤型项⽬的代码⽅⾯，Python 提供了很多选项。熟悉所
有这些选项很重要，这样才能确定哪种项⽬组织⽅式是最佳的，才能理解
别⼈开发的项⽬。

⼀开始应让代码结构尽量简单。⾸先尝试在⼀个⽂件中完成所有的⼯作，
确定⼀切都能正确运⾏后，再将类移到独⽴的模块中。如果你喜欢模块和
⽂件的交互⽅式，可在项⽬开始时就尝试将类存储到模块中。先找出让你
能够编写出可⾏代码的⽅式，再尝试让代码更加整洁。
