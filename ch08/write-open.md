# 读写文件
open() 返回一个 file object ，最常使用的是两个位置参数和一个关键字参数：open(filename, mode, encoding=None)
```python
f = open('workfile', 'w', encoding="utf-8")
```

第一个实参是文件名字符串。第二个实参是包含描述文件使用方式字符的字符串。mode 的值包括 'r' ，表示文件只能读取；'w' 表示只能写入（现有同名文件会被覆盖）；'a' 表示打开文件并追加内容，任何写入的数据会自动添加到文件末尾。'r+' 表示打开文件进行读写。mode 实参是可选的，省略时的默认值为 'r'。

通常情况下，文件是以 text mode 打开的，也就是说，你从文件中读写字符串，这些字符串是以特定的 encoding 编码的。如果没有指定 encoding ，默认的是与平台有关的（见 open() 函数定义 ）。

因为 UTF-8 是现代事实上的标准，除非你知道你需要使用一个不同的编码，否则建议使用 encoding="utf-8" 。在模式后面加上一个 'b' ，可以用 binary mode 打开文件。二进制模式的数据是以 bytes 对象的形式读写的。在二进制模式下打开文件时，你不能指定 encoding 。

在文本模式下读取文件时，默认把平台特定的行结束符 (Unix 上为 \n, Windows 上为 \r\n) 转换为 \n。 在文本模式下写入数据时，默认把 \n 转换回平台特定结束符。 这种操作方式在后台修改文件数据对文本文件来说没有问题，但会破坏 JPEG 或 EXE 等二进制文件中的数据。 注意，在读写此类文件时，一定要使用二进制模式。

在处理文件对象时，最好使用 with 关键字。优点是，子句体结束后，文件会正确关闭，即便触发异常也可以。而且，使用 with 相比等效的 try-finally 代码块要简短得多：
```python
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# 我们可以检测文件是否已被自动关闭。
f.closed
```

如果没有使用 with 关键字，则应调用 f.close() 关闭文件，即可释放文件占用的系统资源。

警告 调用 f.write() 时，未使用 with 关键字，或未调用 f.close()，即使程序正常退出，也**可能** 导致 f.write() 的参数没有完全写入磁盘。

通过 with 语句，或调用 f.close() 关闭文件对象后，再次使用该文件对象将会失败。
```ini
f.close()
f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

f.read(size) 可用于读取文件内容，它会读取一些数据，并返回字符串（文本模式），或字节串对象（在二进制模式下）。 size 是可选的数值参数。省略 size 或 size 为负数时，读取并返回整个文件的内容；文件大小是内存的两倍时，会出现问题。size 取其他值时，读取并返回最多 size 个字符（文本模式）或 size 个字节（二进制模式）。如已到达文件末尾，f.read() 返回空字符串 ('')。

# 读取一行文件内容
f.readline() 从文件中读取单行数据；字符串末尾保留换行符 (\n)，只有在文件不以换行符结尾时，文件的最后一行才会省略换行符。 这种方式让返回值清晰明确；只要 f.readline() 返回空字符串，就表示已经到达了文件末尾，空行使用 '\n' 表示，该字符串只包含一个换行符。

文件中读取多行时，可以用循环遍历整个文件对象。这种操作能高效利用内存，快速，且代码简单
```python
for line in f:
    print(line, end='')
```

# seek方法使用
```python
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)      # 定位到文件中的第 6 个字节

f.read(1)

f.seek(-3, 2)  # 定位到倒数第 3 个字节

f.read(1)
```

f.seek(offset, whence) 可以改变文件对象的位置。通过向参考点添加 offset 计算位置；参考点由 whence 参数指定。 whence 值为 0 时，表示从文件开头计算，1 表示使用当前文件位置，2 表示使用文件末尾作为参考点。省略 whence 时，其默认值为 0，即使用文件开头作为参考点。
```python
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)      # 定位到文件中的第 6 个字节

f.read(1)

f.seek(-3, 2)  # 定位到倒数第 3 个字节

f.read(1)
```
