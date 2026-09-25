# 模块
Python 把各种定义存入一个文件，在脚本或解释器的交互式实例中使用。这个文件就是模块；模块中的定义可以导入到其他模块或主模块（在顶层和计算器模式下，执行脚本中可访问的变量集）。

模块是包含 Python 定义和语句的文件。其文件名是模块名加后缀名 .py 。在模块内部，通过全局变量 __name__ 可以获取模块名（即字符串）。

模块包含可执行语句及函数定义。这些语句用于初始化模块，且仅在 import 语句 第一次 遇到模块名时执行。(文件作为脚本运行时，也会执行这些语句。)

每个模块都有它自己的私有符号表，该表被定义在该模块里的所有函数当作全局符号表使用。 因此，一个模块的作者可以在模块内放心使用全局变量，而不必担心它们会和模块使用者的全局变量发生意外冲突。 另一方面，如果您知道自己在做什么，您可以使用与引用模块函数相同的语法去访问一个模块的全局变量，即 modname.itemname。

```ini
执行python3 进入python终端中
>>> import fibo
>>> fibo.__name__ # 返回模块名字
'fibo'
>>> fibo.fib(12)
0 
1 
1 
2 
3 
5 
8 
>>> fibo.fib2(12)
[0, 1, 1, 2, 3, 5, 8]
```

# 关于import
所有的 import 语句都应放在⽂件开头。唯⼀的例外是，你要在⽂件开头
使⽤注释来描述整个程序。

# 已编译的Python 文件
为了快速加载模块，Python 把模块的编译版本缓存在 __pycache__ 目录中，文件名为 module.version.pyc，version 对编译文件格式进行编码，一般是 Python 的版本号。例如，CPython 的 3.3 发行版中，spam.py 的编译版本缓存为 __pycache__/spam.cpython-33.pyc。这种命名惯例让不同 Python 版本编译的模块可以共存。

Python 对比编译版与源码的修改日期，查看编译版是否已过期，是否要重新编译。此进程完全是自动的。此外，编译模块与平台无关，因此，可在不同架构的系统之间共享相同的库。

Python 在两种情况下不检查缓存。
1. 从命令行直接载入的模块，每次都会重新编译，且不储存编译结果；
2. 没有源模块，就不会检查缓存。为了让一个库能以隐藏源代码的形式分发（通过将所有源代码变为编译后的版本），编译后的模块必须放在源目录而非缓存目录中，并且源目录绝不能包含同名的未编译的源模块。

给专业人士的一些小建议：

在 Python 命令中使用 -O 或 -OO 开关，可以减小编译模块的大小。-O 去除断言语句，-OO 去除断言语句和 __doc__ 字符串。有些程序可能依赖于这些内容，因此，没有十足的把握，不要使用这两个选项。“优化过的”模块带有 opt- 标签，并且文件通常会小一些。将来的发行版或许会改进优化的效果。

从 .pyc 文件读取的程序不比从 .py 读取的执行速度快，.pyc 文件只是加载速度更快。

compileall 模块可以为一个目录下的所有模块创建 .pyc 文件。

# 标准模块
Python 自带一个标准模块的库，它在 Python 库参考（此处以下称为"库参考" ）里另外描述。一些模块是内嵌到解释器里面的，它们给一些虽并非语言核心但却内嵌的操作提供接口，要么是为了效率，要么是给操作系统基础操作例如系统调用提供接口。这些模块集是一个配置选项，并且还依赖于底层的操作系统。

一个特别值得注意的模块 sys，它被内嵌到每一个 Python 解释器中。sys.ps1 和 sys.ps2 变量定义了一些字符，它们可以用作主提示符和辅助提示符:
```ini
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps1 = ">>"
>>sys.ps1=">>>"
```


# 内置函数 dir() 函数
用于查找模块定义的名称。返回结果是经过排序的字符串列表
```ini
>>> import fibo,sys
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_baserepl', '_clear_internal_caches', '_clear_type_cache', '_clear_type_descriptors', '_current_exceptions', '_current_frames', '_debugmallocstats', '_dump_tracelets', '_framework', '_get_cpu_count_config', '_getframe', '_getframemodulename', '_git', '_home', '_is_gil_enabled', '_is_immortal', '_is_interned', '_jit', '_setprofileallthreads', '_settraceallthreads', '_stdlib_dir', '_xoptions', 'abiflags', 'activate_stack_trampoline', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'deactivate_stack_trampoline', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getunicodeinternedsize', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'is_remote_debug_enabled', 'is_stack_trampoline_active', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'monitoring', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'ps1', 'ps2', 'pycache_prefix', 'remote_exec', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions']
```
没有参数时，dir() 列出当前已定义的名称
```ini
>>> dir()
['PS1', 'REPLHooks', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'fibo', 'get_last_command', 'is_wsl', 'original_ps1', 'platform', 'readline', 'sys']
>>> 
```

dir() 不会列出内置函数和变量的名称。这些内容的定义在标准模块 builtins 中
```ini
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '_IncompleteInputError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

# 包
包是通过使用“带点号模块名”来构造 Python 模块命名空间的一种方式。 例如，模块名 A.B 表示名为 A 的包中名为 B 的子模块。 就像使用模块可以让不同模块的作者不必担心彼此的全局变量名一样，使用带点号模块名也可以让 NumPy 或 Pillow 等多模块包的作者也不必担心彼此的模块名冲突。
导入包时，Python 搜索 sys.path 里的目录，查找包的子目录。

需要有 __init__.py 文件才能让 Python 将包含该文件的目录当作包来处理（除非使用 namespace package，这是一个相对高级的特性）。 这可以防止重名的目录如 string 在无意中屏蔽后继出现在模块搜索路径中的有效模块。 在最简单的情况下，__init__.py 可以只是一个空文件，但它也可以执行包的初始化代码或设置 __all__ 变量

从包中导入单个模块
```python
import sound.effects.echo
```
导入子模块的方法
```python
from sound.effects import echo
```

# 从包中导入 *
使用 from sound.effects import * 时会发生什么？你可能希望它会查找并导入包的所有子模块，但事实并非如此。因为这将花费很长的时间，并且可能会产生你不想要的副作用，如果这种副作用被你设计为只有在导入某个特定的子模块时才应该发生。

唯一的解决办法是提供包的显式索引。import 语句使用如下惯例：如果包的 __init__.py 代码定义了列表 __all__，运行 from package import * 时，它就是被导入的模块名列表。发布包的新版本时，包的作者应更新此列表。如果包的作者认为没有必要在包中执行导入 * 操作，也可以不提供此列表。例如，sound/effects/__init__.py 文件可以包含以下代码：
```python
__all__ = ["echo", "surround", "reverse"]
```
这意味着 from sound.effects import * 将导入 sound.effects 包的三个命名子模块

虽然，可以把模块设计为用 import * 时只导出遵循指定模式的名称，但仍不提倡在生产代码中使用这种做法。

# 相对导入
当包由多个子包构成（如示例中的 sound 包）时，可以使用绝对导入来引用同级包的子模块。 例如，如果 sound.filters.vocoder 模块需要使用 sound.effects 包中的 echo 模块，它可以使用 from sound.effects import echo。

你还可以编写相对导入代码，即使用 from module import name 形式的 import 语句。 这些导入使用前导点号来表示相对导入所涉及的当前包和上级包。 例如对于 surround 模块，可以使用:
```python
from . import echo
from .. import formats
from ..filters import equalizer
```
需要注意的是，相对导入是基于当前模块所属包的名称进行的。由于主模块（即直接运行的脚本）没有所属包，因此那些打算作为 Python 应用程序主模块使用的模块，必须始终使用绝对导入。
