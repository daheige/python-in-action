def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
        print()


def fib2(n):
    """Return Fibonacci series up to n."""
    res = []
    a, b = 0, 1
    while a < n:
        res.append(a)
        a, b = b, a + b
    return res


# 以脚本方式执行当前模块
# 运行命令：python3 fibo.py 12
# 这个文件既能被用作脚本，又能被用作一个可供导入的模块，
# 因为解析命令行参数的那两行代码只有在模块作为“main”文件执行时才会运行
if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))
