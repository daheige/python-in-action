# json序列化数据
字符串可以很容易地写入文件或从文件中读取。 数字则更麻烦一些，因为 read() 方法只返回字符串，而字符串必须传给 int() 这样的函数，它接受 '123' 这样的字符串并返回其数值 123。 当你想要保存嵌套列表和字典等更复杂的数据类型时，手动执行解析和序列化操作将会变得非常复杂。

Python 允许你使用流行的数据交换格式 JSON (JavaScript Object Notation)，而不是让用户持续编写和调试代码来将复杂的数据类型存入文件中。 标准库模块 json 可以接受带有层级结构的 Python 数据，并将其转换为字符串表示形式；这个过程称为 serializing。 根据字符串表示形式重建数据则称为 deserializing。 在序列化和反序列化之间，用于代表对象的字符串可以存储在文件或数据库中，或者通过网络连接发送到远端主机。

```python
import json

x = [1, 2, 3]
s = json.dumps(x)
print(s)

# 序列化 dumps
data = {"name": "tom", "age": 20, "hobbies": ["reading", "gaming"]}
s = json.dumps(data, ensure_ascii=False)
print(s)  # {"name": "tom", "age": 20, "hobbies": ["reading", "gaming"]}

# 反序列化：loads ← 字符串
obj = json.loads(s)
print(obj)

# json文件读写：dump / load
# 写入文件
with open("data.json", "w", encoding="utf-8") as f:
    # indent 表示指定缩紧空格
    json.dump(data, f, ensure_ascii=False, indent=2)

obj = {}
with open("data.json", encoding="utf-8") as f:
    obj = json.load(f)

print("obj:", obj)
```
常用参数：
| 参数                   | 作用                      |
| -------------------- | ----------------------- |
| `ensure_ascii=False` | 序列化时保留中文，不转成 `\uXXXX`   |
| `indent=2`           | 格式化输出，缩进 2 个空格          |
| `sort_keys=True`     | 按键名排序                   |
| `default=`           | 序列化时处理不支持的类型（函数）        |
| `object_hook=`       | 反序列化时把 dict 转成自定义对象（函数） |

## 类型对应关系

| Python                 | JSON         |
| ---------------------- | ------------ |
| dict                   | object       |
| list / tuple           | array        |
| str                    | string       |
| int / float            | number       |
| True / False           | true / false |
| None                   | null         |
| set / datetime / 自定义对象 | ❌ 不能直接序列化    |

## 反序列化时还原对象
```python
# 定义对象
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age})"

# 定义钩子函数
def hook(d):
    if "name" in d and "age" in d:
        return User(d["name"], d["age"])
    return d

u = json.loads('{"name": "Tom", "age": 20}', object_hook=hook)
print(u)  # User(name='Tom', age=20)
```

## 常见坑
- json.loads 的输入必须是字符串、bytes 或 bytearray，不能直接读文件对象（用 json.load）。JSON 字符串必须用双引号，单引号 '{"a": 1}' 会报错。
- tuple 序列化后变成 list，反序列化回来是 list，不会还原成 tuple。
- 数字精度：JSON 的 number 反序列化为 Python int/float，非常大的整数可能没问题，但超出 float 精度的浮点数会有精度损失。
- 报错时的典型异常是 json.JSONDecodeError（反序列化失败）。
- 如果是 Web 开发，FastAPI/Flask 里通常直接用框架自带的 JSON 响应处理，底层也是这个模块。
