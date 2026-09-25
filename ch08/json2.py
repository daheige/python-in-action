import json


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
print(u)
