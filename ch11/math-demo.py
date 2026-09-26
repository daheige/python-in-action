#!/usr/bin/env python3
# Python 脚本可以像 shell 脚本一样直接执行，通过在第一行添加上面的说明
import math

print(math.ceil(12 / 5))
print(math.cos(math.pi / 4))
print(math.log2(1024))

# 虽然浮点数无法精确表示其所要代表的实际值，但是可以使用 math.isclose() 函数来进行不精确的值比较
print(math.isclose(0.1 + 0.1 + 0.1, 0.3))
# 或者，也可以使用 round() 函数来大致地比较近似程度
print(round(math.pi, ndigits=2) == round(22 / 7, ndigits=2))
