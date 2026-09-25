from pathlib import Path

path = Path("alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    # 如果文件不存在，就输出错误提示
    print("file not found")
