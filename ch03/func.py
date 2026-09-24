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
