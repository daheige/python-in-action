# 打开文件，第一个参数是文件名，第二个是mode,模式包含r,w,a(追加内容)
# 任何写入的数据会自动添加到文件末尾
# r+表示打开文件进行读写
# mode 参数可选默认是r
#
# python3 read-write.py
fd = open("./test.md", "r", encoding="utf-8")
content = fd.read()  # read 方法不指定size，就表示读取整个文件内容
print(content)
fd.close()

# 以追加的形式写入内容
fd = open("./test.md", "a", encoding="utf-8")
fd.write("\nhello,world")
# 写入其他类型的对象前，要先把它们转化为字符串（文本模式）或字节对象（二进制模式）
value = ("the answer", 21)
s = str(value)  # 先转换为字符串格式，再写入
fd.write("\n" + s)
fd.close()
