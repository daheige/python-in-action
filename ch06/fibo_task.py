# from 从哪个模块导入成员
# import 导入什么元素
# from module import function_name,funtion_name2
from fibo import fib, fib2

fib(12)

f = fib2(12)
print(f)

# 还有一种变体可以导入模块内定义的所有名称
# from fibo import *

# fib(500)
# f = fib2(12)
# print(f)

# as 别名处理
# 对模块名进行别名处理
# import fibo as fib

# fib.fib(500)

# 对 from导入的函数别名处理
# from fibo import fib as fibonacci

# fibonacci(12)
