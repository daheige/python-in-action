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

# vscode python 插件安装
- python 方便写python，以及代码提示和跳转
- ruff 代码格式化处理

## vscode 设置python格式化
- autopep8：较老，基于 PEP 8 规则，改动较保守
- Ruff 用 Rust 编写，速度极快（比 Black 快 10-100 倍），内置 Black 兼容的格式化器，同时可替代 isort、flake8、pylint 等 lint 工具。安装：pip install ruff，使用：ruff format .

## ruff 安装
```shell
pip3 install ruff --break-system-packages
```

推荐使用 autopep8 或 ruff。

## vscode autopep8 配置
```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.autopep8"
  }
}
```

## vscode ruff 配置
关注 python 和 ruff 配置，以及 editor.formatOnSave 即可
```json
{
    "editor.fontSize": 16,
    "workbench.colorTheme": "Monokai",
    "hediet.vscode-drawio.resizeImages": null,
    "rust-analyzer.rustfmt.rangeFormatting.enable": true,
    "[rust]": {
        "editor.defaultFormatter": "rust-lang.rust-analyzer",
        "editor.formatOnSave": true,
        "editor.inlayHints.enabled": "off"
    },
    "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.codeActionsOnSave": {
            "source.fixAll.ruff": "explicit",
            "source.organizeImports.ruff": "explicit"
        }
    },
    // 保存时自动修复 + 整理 import
    "ruff.organizeImports": true,
    "ruff.fixAll": true,
    // // 导入排序风格（可选）
    "ruff.configurationPreference": "editorOnly",
    // 指定 Python 解释器（多环境时有用）
    "ruff.interpreter": [
        ".venv/bin/python"
    ],
    "editor.unicodeHighlight.nonBasicASCII": false,
    "claudeCode.preferredLocation": "panel",
    "go.toolsManagement.autoUpdate": true,
    "editor.formatOnSave": true
}
```

## ruff 项目级配置（可选但推荐）
在项目根目录建 pyproject.toml 或 ruff.toml
```toml
[tool.ruff]
target-version = "py312"
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]

[tool.ruff.lint.isort]
known-first-party = ["my_project"]
```

# uv 工具安装 (用于python包管理)
uv 的优势如下：
- 速度极快：由于使用 Rust 编写，uv 的性能远超 pip 和其他包管理工具，安装依赖的速度可以提升 10-100 倍。
- 功能集成：集成语法分析、依赖解析、包安装、环境管理和 Python 版本管理于一体，无需再安装和学习多个工具。
- 确定性构建：uv 会生成 uv.lock 文件，确保在任何环境中都能安装完全相同的依赖版本，避免 "在我机器上能运行" 的问题。
- 与现有工具兼容：uv 可以处理 requirements.txt 和 pyproject.toml，可以无缝替代现有工作流中的 pip。

```shell
pip3 install uv --break-system-packages
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

退出虚拟环境命令
```shell
echo $VIRTUAL_ENV   # 有输出说明在虚拟环境中

# 退出虚拟环境
deactivate
```

# python 教程
- 书籍：Python编程从入门到实践第3版 pdf网上可下载
- 配套教程：https://www.bilibili.com/video/BV1nqgY6pEuf
- 官方教程：https://docs.python.org/zh-cn/3.14/tutorial/index.html

# python 标准库
https://docs.python.org/zh-cn/3.13/library/index.html#library-index

# python 参考手册
https://docs.python.org/zh-cn/3.13/reference/index.html#reference-index
