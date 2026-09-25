import json
from pathlib import Path


def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"welcome back,{username}")
    else:
        username = get_new_username(path)
        print(f"we'll remember you,when you come back,{username}")


def get_new_username(path):
    username = input("input your name?")
    contents = json.dumps(username)
    path.write_text(contents)


def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


greet_user()
