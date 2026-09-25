import json

x = [1, 2, 3]
s = json.dumps(x)
print(s)

# 序列化 dumps
data = {"name": "tom", "age": 20, "hobbies": ["reading", "gaming"]}
# 序列化时保留中文，不转成 \uXXXX
s = json.dumps(data, ensure_ascii=False)
print(s)  # {"name": "tom", "age": 20, "hobbies": ["reading", "gaming"]}

# 反序列化：loads ← 字符串
obj = json.loads(s)
print(obj)

# json文件读写：dump / load
# 写入文件
with open("data.json", "w", encoding="utf-8") as f:
    # indent 表示格式化输出，缩进 2 个空格
    json.dump(data, f, ensure_ascii=False, indent=2)

obj = {}
with open("data.json", encoding="utf-8") as f:
    obj = json.load(f)

print("obj:", obj)

# 时间格式处理
from datetime import datetime


def default_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, set):
        return list(obj)
    raise TypeError(f"不可序列化类型: {type(obj)}")


# {"time": "2026-09-25T21:47:00.743150"}
print(json.dumps({"time": datetime.now()}, default=default_handler))
