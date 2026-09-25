# 使用from+import关键字导入特定的成员
# from 表示从哪个模块导入
# 格式： from module_name import function_name,function_name2
# 显式地导⼊了 make_pizza() 和 make_pizza2 函数
# from pizza import make_pizza, make_pizza2

# # 调用模块中的函数
# make_pizza("x", "y")
# make_pizza2(12, "x", "y", "z")

# 使用 as 关键字给导入的成员别名处理
# from pizza import make_pizza as mpizza
# from pizza import make_pizza2 as mpizza2

# # 调用模块中的函数
# mpizza("x", "y")
# mpizza2(12, "x", "y", "z")

# 使⽤ as 给模块指定别名
# import pizza as p

# p.make_pizza("x", "y")
# p.make_pizza2(12, "x", "y", "z")


# 导入模块中的所有成员
# 使⽤星号（*）运算符可让 Python 导⼊模块中的所有函数
"""
由于导⼊了每个函数，可通过名称来调⽤每个函数，⽆须使
⽤点号（dot notation）。然⽽，在使⽤并⾮⾃⼰编写的⼤型模块时，最好不
要使⽤这种导⼊⽅法，因为如果模块中有函数的名称与当前项⽬中既有的
名称相同，可能导致意想不到的结果：Python 可能会因为遇到多个名称相
同的函数或变量⽽覆盖函数，⽽不是分别导⼊所有的函数

最佳的做法是，要么只导⼊需要使⽤的函数，要么导⼊整个模块并使⽤点
号。这都能让代码更清晰，更容易阅读和理解。
"""

from pizza import *

make_pizza("x", "y")
make_pizza2(12, "x", "y", "z")
