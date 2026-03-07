# python-in-action
python in action

# python 虚拟环境
创建并激活一个虚拟环境，可以避免直接修改系统 Python 环境
```shell
# 创建虚拟环境
python3 -m venv myenv

# 激活虚拟环境
source myenv/bin/activate

# 现在可以安全地使用 pip 安装包
pip install xxx

# 退出虚拟环境
deactivate
```

# pip3 使用
如果你确实需要在系统环境中安装包，可以使用 --break-system-packages 参数绕过限制，但需注意这可能会破坏系统 Python 环境：
```shell
pip3 install --break-system-packages package_name
# 实例如下：
# pip3 install --break-system-packages ruff
```

# vscode 设置python格式化
```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```
或者使用auto
```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.autopep8"
  }
}
```

# uv工具安装
```shell
pip install uv
```
后续就可以通过uv工具来安装对应的python包
```shell
uv pip install redis
```

# python 教程
https://docs.python.org/zh-cn/3.13/tutorial/index.html

https://docs.python.org/zh-cn/3.13/tutorial/introduction.html

# python 标准库
https://docs.python.org/zh-cn/3.13/library/index.html#library-index

# python 参考手册
https://docs.python.org/zh-cn/3.13/reference/index.html#reference-index
