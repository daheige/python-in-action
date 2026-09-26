import unittest


def average(s):
    return sum(s) / len(s)


# 允许在一个单独的文件中维护更全面的测试集
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)


unittest.main()  # 从命令行调用时会执行所有测试
