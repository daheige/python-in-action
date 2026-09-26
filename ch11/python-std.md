# python 语言标准库
https://docs.python.org/zh-cn/3.14/tutorial/stdlib.html

python 语言内置了 `os`,`sys`,`pathlib`等标准库，用于快速开发程序。

# os 操作系统接口
os 提供了很多和操作系统交互的函数
```python
import os
import subprocess

print(os.getcwd())  # 获取当前目录
# 执行系统shell命令
# os.system("top")
# 使用subprocess替代system
subprocess.run("ls", check=False)
```
一定要使用 import os 而不是 from os import * 。这将避免内建的 open() 函数被 os.open() 隐式替换掉，因为它们的使用方式大不相同。

内置的 dir() 和 help() 函数可用作交互式辅助工具，用于处理大型模块，如 os
```python
import os
# 返回由模块的所有函数组成的列表
dir(os)

# 返回根据模块文档字符串创建的详细说明页面
help(os)
```

# shutil
对于日常文件和目录管理任务，shutil 模块提供了更易用的高层级接口
```python
import shutil
# 复制文件
shutil.copyfile('data.db', 'archive.db')

# 移动文件
shutil.move('/build/executables', 'installdir')
```

# glob
glob 模块提供了一个在目录中使用通配符搜索创建文件列表的函数
```python
import glob
# 列出所有python文件
glob.glob('*.py')
```

# 命令行参数
通用工具脚本往往需要处理命令行参数。 这些参数以列表形式存储在 sys 模块的 argv 属性中。 举例来说，让我们查看下面的 demo.py 文件:
```python
import sys

# python3 demo.py 1 2 3
# 传递的cli参数是： ['demo.py', '1', '2', '3']
print("传递的cli参数是：", sys.argv)
```

argparse 模块提供了一种更复杂的机制来处理命令行参数。 以下脚本可提取一个或多个文件名并可选择要显示的行数:

```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```
当通过 python top.py --lines=5 alpha.txt beta.txt 在命令行运行时，该脚本会将 args.lines 设为 5 并将 args.filenames 设为 ['alpha.txt', 'beta.txt']

# 错误输出重定向和程序终止
sys 模块还具有 stdin ， stdout 和 stderr 的属性。后者对于发出警告和错误消息非常有用，即使在 stdout 被重定向后也可以看到它们
```python
import sys
sys.stderr.write('Warning, log file not found starting a new one\n')
```
输出到错误终端：Warning, log file not found starting a new one

# 字符串模式匹配
re 模块为高级字符串处理提供正则表达式工具。对于复杂的匹配和操作，正则表达式提供简洁，优化的解决方案
```python
import re

# 正则查找
s = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest")
print(s)
s1 = re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat")
print(s1)
```

当只需要简单的功能时，首选字符串方法因为它们更容易阅读和调试:
```python
s = "tea for too".replace("too","two")
print(s)
```

# 数学模块 math
math 模块提供对用于浮点数学运算的下层 C 库函数的访问
```python
import math

print(math.ceil(12 / 5))
print(math.cos(math.pi / 4))
print(math.log2(1024))
```

# random
random 模块提供了进行随机选择的工具
```python
import random

random.randrange(6)     # 0~5，等价于 randrange(0, 6)
random.randrange(1, 6)  # 1~5（不含 6）
random.randint(0, 5)    # 0~5，效果同上
random.random()         # 0.0~1.0 的浮点数，注意别混淆

print(random.choice(["a", "b", "c"]))  # 随机返回列表中的一个元素

s = random.sample(range(100), 10)  # 随机返回10个100之内的数字
print(s)

# 返回[0.0,1.0] 区间的随机浮点数
f = random.random()
print(f)

# 从range(6) 返回0-5之间的数字
# random.randrange(6) 等价于 random.randrange(0, 6)，
# 返回 [0, 5] 之间的整数（含 0 和 5）
number = random.randrange(6)
print(number)
```
容易踩的坑：randint(a, b) 和 randrange(a, b) 不一样——randint 含右端点，randrange 不含右端点：
```python
print(random.randint(0, 6))  # 0~6，可能返回 6！
print(random.randrange(0, 6))  # 0~5，绝不会返回 6
```

# statistics 模块
计算数值数据的基本统计属性（均值，中位数，方差等）
```python
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)

statistics.median(data)

statistics.variance(data)
```

# 互联网访问
有许多模块可用于访问互联网和处理互联网协议。其中两个最简单的 urllib.request 用于从URL检索数据，以及 smtplib 用于发送邮件:
```python
from urllib.request import urlopen

# 发送请求
# 输出 Last updated on Sep 26, 2026 (02:42 UTC).
with urlopen("https://docs.python.org/3/") as response:
    for line in response:
        line = line.decode()
        if "updated" in line:
            print(line.rstrip())
```
发送邮件
```python
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()
```

# 日期和时间
datetime 模块提供了以简单和复杂的方式操作日期和时间的类。虽然支持日期和时间算法，但实现的重点是有效的成员提取以进行输出格式化和操作。该模块还支持可感知时区的对象。
```python
import datetime as dt

now = dt.date.today()  # 今天  # noqa: DTZ011
print(now)

# 格式化输出
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = dt.date(1964, 7, 31)
age = now - birthday
print(age.days)
```

# 数据压缩
常见的数据存档和压缩格式由模块直接支持，包括：zlib, gzip, bz2, lzma, zipfile 和 tarfile
```python
import zlib

s = b"witch which has which witches wrist watch"
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))

print(zlib.crc32(s))
```

# 性能测量 timeit
例如，元组封包和拆包功能相比传统的交换参数可能更具吸引力。timeit 模块可以快速演示在运行效率方面一定的优势:
```python
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
Timer('a,b = b,a', 'a=1; b=2').timeit()
```

# 质量控制

开发高质量软件的一种方法是在开发过程中为每个函数编写测试，并在开发过程中经常运行这些测试

doctest 模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试。测试构造就像将典型调用及其结果剪切并粘贴到文档字符串一样简单。这通过向用户提供示例来改进文档，并且它允许 doctest 模块确保代码与文档保持一致:

```python
import doctest

doctest.testmod()  # 自动验证嵌入式测试


def average(values):
    """计算数字列表的算术平均值

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)
```
unittest 模块不像 doctest 模块那样易于使用，但它允许在一个单独的文件中维护更全面的测试集:
```python
import unittest


def average(s):
    return sum(s) / len(s)


class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)


unittest.main()  # 从命令行调用时会执行所有测试
```

# 内置电池
Python 有"自带电池"的理念。通过其包的复杂和强大功能可以最好地看到这一点。例如:

- xmlrpc.client 和 xmlrpc.server 模块使得实现远程过程调用变成了小菜一碟。 尽管存在于模块名称中，但用户不需要直接了解或处理 XML。
- email 包是一个用于管理电子邮件消息的库，包括 MIME 和其他基于 RFC 5322 的消息文档。 不同于实际发送和接收消息的 smtplib 和 poplib，email 包提供用于构建或解码复杂消息结构（包括附件）以及实现互联网编码格式和标头协议的完整工具集。
- json 包为解析这种流行的数据交换格式提供了强大的支持。
- csv 模块支持以逗号分隔值格式直接读取和写入文件，这种格式通常为数据库和电子表格所支持。
- XML 处理由 xml.etree.ElementTree，xml.dom 和 xml.sax 包支持。这些模块和软件包共同大大简化了 Python 应用程序和其他工具之间的数据交换。
- sqlite3 模块是 SQLite 数据库库的包装器，提供了一个可以使用稍微非标准的 SQL 语法更新和访问的持久数据库。
- 国际化由许多模块支持，包括 gettext，locale ，以及 codecs 包。
