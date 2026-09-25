import json
from pathlib import Path

numbers = [1, 2, 3, 4, 5]
path = Path("number.json")
contents = json.dumps(numbers)  # 序列化处理
# 将内容写入文件中
path.write_text(contents)
