import doctest

doctest.testmod()  # 自动验证嵌入式测试


def average(values):
    """计算数字列表的算术平均值

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)
