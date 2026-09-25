# 从 car.py 模块中导入成员
from car import Car, EleCar2, ElectricCar

my_car = Car("audi", "a4", 2024)
my_car.read_odometer()
# 修改类成员属性值
my_car.odometer_reading = 100  # 直接修改属性的值
my_car.read_odometer()

my_car.update_odometer(121)
my_car.read_odometer()

my_car.update_odometer(120)
my_car.read_odometer()
my_car.increment_odometer(12)
my_car.read_odometer()

# 创建子类实例对象
ele_car = ElectricCar("ele", "a1", 2026)
ele_car.read_odometer()
ele_car.run()
ele_car.desc_battery_size()
ele_car.update_battery_size(13)
ele_car.desc_battery_size()
ele_car.fill_gas_tank()

# 创建组合类型的实例对象
my_leaf = EleCar2("nissan", "leaf", 2025)
print(my_leaf.get_descriptive_name())
