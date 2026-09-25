# python 提供了 pathlib 模块，让开发者可以轻松的处理不同操作系统的文件和目录操作

from pathlib import Path

path = Path("./test.md")  # 相对路径
contents = path.read_text().rstrip()  # 读取文本，去掉右边的空白
print(contents)

print("readlines")
# 访问文件的各行内容
path = Path("./test.md")  # 相对路径
contents = path.read_text()
lines = contents.splitlines()
pi_str = ""
for line in lines:
    print(line.rstrip())
    pi_str += line.rstrip()

# 一行输出
print(pi_str)
