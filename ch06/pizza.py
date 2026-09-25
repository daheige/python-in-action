# 将函数存储在模块中
# 传递任意数量的实参
# 在函数定义前面加上*
# make_pizza("m", "n", "x", "y")  # ('m', 'n', 'x', 'y') 本质上toppings是一个元组
def make_pizza(*toppings):
    print(toppings)


# 任意参数只能放在最后
"""
如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实
参的形参放在最后。Python 先匹配位置实参和关键字实参，再将余下的实
参都收集到最后⼀个形参中
"""


# make_pizza2(12, "x", "y", "z")
def make_pizza2(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for t in toppings:
        print(f"- {t}")
