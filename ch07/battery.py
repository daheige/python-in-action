# 组合
# 通过定义 Battery 类，将电动车的功能属性，以组合的方式嵌入到 EleCar2 类中
class Battery:
    # 初始化类的时，成员变量也可以指定默认值
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def desc_battery_size(self):
        print(f"this ele car battery_size is {self.battery_size}")
