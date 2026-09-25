# 定义没有参数的函数
# 通过三个引号注释函数
# 使⽤关键字 def 定义函数
def greet():
    """
    show simple greeter
    """
    print("hello,world")


greet()


# 实参和形参
# name 是形参
# 在调用函数的实际参数是实参
# name 是一个字符串
def greet_user(name: str):
    """
    show simple greeter
    """
    print(f"hello,{name}")


greet_user("daheige")
greet_user("alex")


# 定义函数可以给参数指定默认值
def hello(name="world"):
    print(f"hello,{name}")


hello()


# 函数返回值
def upper(name: str):
    return name.upper()


print(upper("daheige"))  # DAHEIGE


def build_person(first_name, last_name):
    """返回一个字典，其中包含个人信息"""
    person = {
        "first": first_name,
        "last": last_name,
    }
    return person


print(build_person("da", "heige"))


def greet_names(names: list):
    for name in names:
        msg = f"hello,{name.title()}"
        print(msg)


greet_names(["alex", "daheige"])


# 传递任意数量的实参
# 在函数定义前面加上*
def make_pizza(*toppings):
    print(toppings)


make_pizza("m", "n", "x", "y")  # ('m', 'n', 'x', 'y') 本质上toppings是一个元组

# 任意参数只能放在最后
"""
如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实
参的形参放在最后。Python 先匹配位置实参和关键字实参，再将余下的实
参都收集到最后⼀个形参中
"""


def make_pizza2(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for t in toppings:
        print(f"- {t}")


make_pizza2(12, "x", "y", "z")


# 函数定义时，可以给默认参数
def ask_ok(prompt, retries=4, reminder="please try again"):
    while True:
        # input 表示接收用户输入
        reply = input(prompt)
        if reply in {"y", "ye", "yes", "Y"}:
            return True
        if reply in {"n", "no", "N", "nop", "nope"}:
            return False
        retries -= 1
        if retries < 0:
            raise ValueError("invalid user reply")
        print(reminder)


# ask_ok("do you really want to quit?")

# 这样的方式L底层会共享
# def f(a, L=[]):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

"""
print(f(1))
print(f(2))
print(f(3))
[1]
[1, 2]
[1, 2, 3]
"""


# 底层不共享
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


# 关键字参数
# 关键字实参是传递给函数的名值对。这样会直接在实参中将名称和值关联起来
# 关键字实参不仅让你⽆须考虑函数调⽤中的实参顺
# 序，⽽且清楚地指出了函数调⽤中各个值的⽤途
#
# kwarg=value 形式的 关键字参数 也可以用于调用函数。函数示例如下
# 其实就是给参数命名
def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# 调用函数时，不一定按照函数参数顺序传递，而是通过名字指定参数赋值
parrot(voltage=100, action="vm", state="up")


# 任意实参列表
# *args 形参后的任何形式参数只能是仅限关键字参数，即只能用作关键字参数，不能用作位置参数
def concat(*args, sep="/"):
    return sep.join(args)


s = concat("a", "b", "c", sep="@")
print(s)

# 解包实参列表
s = list(range(1, 5))
print(s)

args = [3, 6]
s = list(range(*args))  # 用 * 操作符把实参从列表或元组解包出来
print(s)


# lambda 表达式
# lambda 关键字用于创建小巧的匿名函数
# 在语法上，匿名函数只能是单个表达式。
# 在语义上，它只是常规函数定义的语法糖。与嵌套函数定义一样，lambda 函数可以引用包含作用域中的变量
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(12)
n = f(1)
print(n)

# lambda作为参数
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
# 按照切片的第1个下标成员进行排序
pairs.sort(key=lambda pair: pair[1])
print(pairs)


# 文档字符串，给函数加注释
def my_func():
    """
    do nothing,bu document it
    """


print(my_func.__doc__)  # 获取函数文档字符串


# 给函数定义的参数指定类型，并返回值
# 这里函数的返回值使用->方式，返回出参
def foo(ham: str, eggs: str = "eggs") -> str:
    # 输出函数定义的额元信息  {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
    print("Annotations:", foo.__annotations__)
    print("args:", ham, eggs)
    return ham + " and " + eggs


s = foo("spam")
print(s)
