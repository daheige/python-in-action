from pathlib import Path

path = Path("programming.txt")
# 在对 path 对象调⽤ write_text() ⽅法时，务必谨慎。如果
# 指定的⽂件已存在， write_text() 将删除其内容，并将指定的内容
# 写⼊其中
# path.write_text("hello,world")

# 写入多行文本
contents = "hello,python\n"
contents += "hello,go\n"
contents += "hello,rust\n"

path.write_text(contents)
