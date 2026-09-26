# 错误和异常
错误可（至少）被分为两种：语法错误 和 异常。

1. 语法错误又称解析错误，是学习 Python 时最常见的错误。
2. 异常，即使语句或表达式使用了正确的语法，执行时仍可能触发错误。执行时检测到的错误称为 异常，异常不一定导致严重的后果。

# 异常的处理
通过 try...except处理异常。
```python
x = 0
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

print("x:", x)
```

一条 try 语句可以有多个 except 子句，以便为不同的异常指定处理器。 但最多只有一个处理器会被执行。 处理器只处理对应 try 子句 中发生的异常，而不处理同一 same try 子句内其他处理器中的异常。 一个 except 子句 可以指定多个异常，例如:
```python
except RuntimeError, TypeError, NameError:
    pass
```
一个 except 子句中的类匹配的异常将是该类本身的实例或其所派生的类的实例（但反过来则不可以 --- 列出派生类的 except 子句 不会匹配其基类的实例）。例如，下面的代码将依次打印 B, C, D:
```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```
raise cls() 的作用是：主动抛出一个异常实例。cls 是异常类（B、C、D），cls() 是实例化出一个异常对象，raise 把它抛出来。

这里 raise 是人为制造异常来测试异常匹配逻辑，实际代码中通常是抛出并带个消息：raise ValueError("输入不合法")

请注意如果颠倒 except 子句 的顺序（把 except B 放在最前），则会输出 B, B, B --- 即触发了第一个匹配的 except 子句。

发生异常时，它可能具有关联值，即异常 参数 。是否需要参数，以及参数的类型取决于异常的类型。

except 子句 可能会在异常名称后面指定一个变量。这个变量将被绑定到异常实例，该实例通常会有一个存储参数的 args 属性。 为了方便起见，内置异常类型定义了 __str__() 来打印所有参数而不必显式地访问 .args。
```python
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # 异常的类型
    print(inst.args)     # 参数保存在 .args 中
    print(inst)          # __str__ 允许 args 被直接打印，
                         # 但可能在异常子类中被覆盖
    x, y = inst.args     # 解包 args
    print('x =', x)
    print('y =', y)
```
未处理异常的 __str__() 输出会被打印为该异常消息的最后部分 ('detail')。

BaseException 是所有异常的共同基类。它的一个子类，Exception，是所有非致命异常的基类。不是 Exception 的子类的异常通常不被处理，因为它们被用来指示程序应该终止。它们包括由 sys.exit() 引发的 SystemExit，以及当用户希望中断程序时引发的 KeyboardInterrupt。

Exception 可以被用作通配符，捕获（几乎）一切。然而，好的做法是，尽可能具体地说明我们打算处理的异常类型，并允许任何意外的异常传播下去。

处理 Exception 最常见的模式是打印或记录异常，然后重新提出（允许调用者也处理异常）
```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```
如果文件不存在，运行效果如下：
```ini
OS error: [Errno 2] No such file or directory: 'myfile.txt'
```

try ... except 语句具有可选的 else 子句，该子句如果存在，它必须放在所有 except 子句 之后。它适用于 try 子句 没有引发异常但又必须要执行的代码。例如:
```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```
使用 else 子句比向 try 子句添加额外的代码要好，可以避免意外捕获非 try ... except 语句保护的代码触发的异常。

异常处理程序不仅会处理在 try 子句 中立刻发生的异常，还会处理在 try 子句 中调用（包括间接调用）的函数。例如:
```python
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
```

# 触发异常
raise 语句支持强制触发指定的异常。例如：
```python
raise NameError('HiThere')
```
raise 唯一的参数就是要触发的异常。这个参数必须是异常实例或异常类（派生自 BaseException 类，例如 Exception 或其子类）。如果传递的是异常类，将通过调用没有参数的构造函数来隐式实例化：

# 异常链
如果一个未处理的异常发生在 except 部分内，它将会有被处理的异常附加到它上面，并包括在错误信息中
```python
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
```

为了表明一个异常是另一个异常的直接后果， raise 语句允许一个可选的 from 子句:
```python
# exc 必须为异常实例或为 None。
raise RuntimeError from exc
```
转换异常时，这种方式很有用。例如：
```python
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
```
它还允许使用 from None 表达禁用自动异常链:
```python
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
```

# 用户自定义异常
程序可以通过创建新的异常类命名自己的异常 (Python 类的内容详见 类)。 不论是以直接还是间接的方式，异常都应从 Exception 类派生。

异常类可以被定义成能做其他类所能做的任何事，但通常应当保持简单，它往往只提供一些属性，允许相应的异常处理程序提取有关错误的信息。

大多数异常命名都以"Error"结尾，类似标准异常的命名。

许多标准模块定义了自己的异常，以报告他们定义的函数中可能出现的错误。

# 定义清理操作
try 语句还有一个可选子句，用于定义在所有情况下都必须要执行的清理操作。例如：
```python
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
```
如果存在 finally 子句，则 finally 子句是 try 语句结束前执行的最后一项任务。不论 try 语句是否触发异常，都会执行 finally 子句。以下内容介绍了几种比较复杂的触发异常情景：
- 如果执行 try 子句期间触发了某个异常，则某个 except 子句应处理该异常。如果该异常没有 except 子句处理，在 finally 子句执行后会被重新触发。
- except 或 else 子句执行期间也会触发异常。同样，该异常会在 finally 子句执行之后被重新触发。
- 如果 finally 子句执行 break、 continue 或 return 语句，异常不重新引发。这可能会引起混淆，因此不鼓励使用。从 3.14 版开始，编译器会为它发出一个 SyntaxWarning (参见 PEP 765)。
- 如果执行 try 语句时遇到 break、continue 或 return 语句，则 finally 子句在执行 break、continue 或 return 语句之前执行。
- 如果一个 finally 子句包含一个 return 语句，返回的值将是来自 finally 子句的 return 语句，而不是来自 try 子句的 return 语句。 这可能会引起混淆，因此不提倡使用。 从 3.14 版开始，编译器会为它发出一个 SyntaxWarning (参见 PEP 765)。

```python
def bool_return():
    try:
        return True
    finally:
        return False

bool_return()
# False
```

# 预定义的清理操作
with 语句支持以及时、正确的清理的方式使用文件对象：
```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```
语句执行完毕后，即使在处理行时遇到问题，都会关闭文件 f。和文件一样，支持预定义清理操作的对象会在文档中指出这一点。

# 引发和处理多个不相关的异常
在有些情况下，有必要报告几个已经发生的异常。这通常是在并发框架中当几个任务并行失败时的情况，但也有其他的用例，有时需要是继续执行并收集多个错误而不是引发第一个异常。

内置的 ExceptionGroup 打包了一个异常实例的列表，这样它们就可以一起被引发。它本身就是一个异常，所以它可以像其他异常一样被捕获。
```python
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

f()

try:
    f()
except Exception as e:
    print(f'caught {type(e)}: {e}')
```
通过使用 except* 代替 except ，我们可以有选择地只处理组中符合某种类型的异常。在下面的例子中，显示了一个嵌套的异常组，每个 except* 子句都从组中提取了某种类型的异常，而让所有其他的异常传播到其他子句，并最终被重新引发。
```python
def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
```
注意，嵌套在一个异常组中的异常必须是实例，而不是类型。这是因为在实践中，这些异常通常是那些已经被程序提出并捕获的异常，其模式如下:
```python
excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Test Failures", excs)
```

# 用注释细化异常情况
当一个异常被创建以引发时，它通常被初始化为描述所发生错误的信息。在有些情况下，在异常被捕获后添加信息是很有用的。为了这个目的，异常有一个 add_note(note) 方法接受一个字符串，并将其添加到异常的注释列表。标准的回溯在异常之后按照它们被添加的顺序呈现包括所有的注释。

```python
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise
```
```ini
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise TypeError('bad type')
TypeError: bad type
Add some information
Add some more information
```
例如，当把异常收集到一个异常组时，我们可能想为各个错误添加上下文信息。在下文中，组中的每个异常都有一个说明，指出这个错误是什么时候发生的。
```python
def f():
    raise OSError('operation failed')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('We have some problems', excs)
```
