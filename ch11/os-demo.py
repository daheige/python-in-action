import glob
import os
import shutil
import subprocess

print(os.getcwd())  # 获取当前目录
# 执行系统shell命令
# os.system("top")
# 使用subprocess替代system
subprocess.run("ls", check=False)

shutil.copyfile("test.md", "test1.md")

# glob 模块提供了一个在目录中使用通配符搜索创建文件列表的函数
print(glob.glob("*.py"))
