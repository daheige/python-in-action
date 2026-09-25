# 从一个模块中导入另一个模块
from battery import Battery


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 里程，给成员定义默认值

    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"this car {self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")

    # 通过⽅法修改属性的值
    def update_odometer(self, m):
        if m >= self.odometer_reading:
            self.odometer_reading = m
        else:
            print("you can't roll back this odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("this car has gas")


# 在⼀个模块中存储多个类
# 电动车继承了Car
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 40  # 给子类添加成员，电池容量

    # 给子类添加方法
    def run(self):
        print("electric car running...")

    def update_battery_size(self, size):
        self.battery_size = size

    def desc_battery_size(self):
        print(f"this ele car battery_size is {self.battery_size}")

    # 重写父类中的方法
    def fill_gas_tank(self):
        print("this car has no gas")


# 组合
class EleCar2(Car):
    def __init__(self, make, model, year):
        """
        每当 __init__() ⽅法被调⽤时，都将执⾏该操作，
        因此现在每个 EleCar2 实例都包含⼀个⾃动创建的 Battery 实例。
        """
        super().__init__(make, model, year)
        self.battery = Battery()
