# 导入整个模块
import car

my_car = car.Car("audi", "a4", 2026)
my_car.update_odometer(12)
my_car.read_odometer()
print(my_car.get_descriptive_name())

my_leaf = car.EleCar2("nis", "leaf", 2026)
# 调用组合类 Battery 实例对象上的方法
my_leaf.battery.desc_battery_size()
