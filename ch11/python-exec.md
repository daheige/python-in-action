# 可执行的 Python 脚本
在 BSD 等类 Unix 系统上，Python 脚本可以像 shell 脚本一样直接执行，通过在第一行添加：
```python
#!/usr/bin/env python3
```
比如：
```shell
➜  ch11 git:(main) ✗ chmod +x math-demo.py 
➜  ch11 git:(main) ✗ ./math-demo.py 
3
0.7071067811865476
10.0
True
True
```
