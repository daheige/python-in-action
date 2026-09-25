# 异常处理
Python 使⽤称为异常（exception）的特殊对象来管理程序执⾏期间发⽣的
错误。每当发⽣让 Python 不知所措的错误时，它都会创建⼀个异常对象。
如果你编写了处理该异常的代码，程序将继续运⾏；如果你未对异常进⾏
处理，程序将停⽌，并显⽰⼀个 traceback，其中包含有关异常的报告。

异常是使⽤ try-except 代码块处理的。try-except 代码块让 Python
执⾏指定的操作，同时告诉 Python 在发⽣异常时应该怎么办。在使⽤
try-except 代码块时，即便出现异常，程序也将继续运⾏：显⽰你编写
的友好的错误消息，⽽不是令⽤户迷惑的 traceback。

# 处理 ZeroDivisionError 异常
```python
print(5/0)
```
```ini
print(5/0)
Traceback (most recent call last):
  File "<python-input-18>", line 1, in <module>
    print(5/0)
          ~^~
ZeroDivisionError: division by zero
```
# 使⽤ try-except 代码块
如果 try-except 代码块后⾯还有其他代码，程序将继续运⾏，因为
Python 已经知道了如何处理错误。
```python
# try-except语句
try:
    print(5 / 0)
except ZeroDivisionError:
    # 异常处理逻辑
    print("divide invalid")
```

# else 代码块
通过将可能引发错误的代码放在 try-except 代码块中，可提⾼程序抵御
错误的能⼒。因为错误是执⾏除法运算的代码⾏导致的，所以需要将它放
到 try-except 代码块中。这个⽰例还包含⼀个 else 代码块，只有 try
代码块成功执⾏才需要继续执⾏的代码，都应放到 else 代码块中。

```python
number = input("input number:")
try:
    num = int(number)
except:  # noqa: E722
    print("invalid number")
else:
    print(num)
```
依赖 try 代码块成功执⾏的代码都被放在 else 代码块中。在这个⽰例中，如果除法运算成功，就使⽤ else 代码块来打印结果

# 处理 FileNotFoundError 异常
文件不存在读取例子如下：
```python
from pathlib import Path

path = Path("alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    # 如果文件不存在，就输出错误提示
    print("file not found")
```

# 静默失败
可以通过pass关键字，在except中占位即可
