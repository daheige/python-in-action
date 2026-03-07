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
推荐使用autopep8
```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.autopep8"
  }
}
```

# uv工具安装
uv 的优势
- 速度极快：由于使用 Rust 编写，uv 的性能远超 pip 和其他包管理工具，安装依赖的速度可以提升 10-100 倍。
- 功能集成：集成语法分析、依赖解析、包安装、环境管理和 Python 版本管理于一体，无需再安装和学习多个工具。
- 确定性构建：uv 会生成 uv.lock 文件，确保在任何环境中都能安装完全相同的依赖版本，避免 "在我机器上能运行" 的问题。
- 与现有工具兼容：uv 可以处理 requirements.txt 和 pyproject.toml，可以无缝替代现有工作流中的 pip。

```shell
pip install uv
```
后续就可以通过uv工具来安装对应的python包
```shell
uv pip install redis
```
uv使用文档：https://www.runoob.com/python3/uv-tutorial.html

# 通过uv 创建虚拟环境
```shell
# 创建名为 .venv 的虚拟环境（默认）
uv venv

# 激活环境（macOS/Linux）
source .venv/bin/activate

# 激活环境（Windows）
.venv\Scripts\activate
```

# python 教程
推荐书籍：
- 基础入门《Python基础教程（第3版·修订版）（图灵出品）》 和 《Python编程 从入门到实践 第3版（图灵出品）》作为基础知识入门即可
- python运维自动化：《Python自动化运维快速入门（第2版）》
- ai agent开发：《AI Agent开发实战：从基础原理到企业级应用》，同时推荐《AI工程》掌握ai相关的基础知识

# python官方基础入门文档
- https://docs.python.org/zh-cn/3.13/tutorial/index.html
- https://docs.python.org/zh-cn/3.13/tutorial/introduction.html

# python 标准库
https://docs.python.org/zh-cn/3.13/library/index.html#library-index

# python 参考手册
https://docs.python.org/zh-cn/3.13/reference/index.html#reference-index
