import argparse

# python3 argparse-demo.py --lines=5 a.txt b.txt
# Namespace(filenames=['a.txt', 'b.txt'], lines=5)
parser = argparse.ArgumentParser(
    prog="top", description="show top lines from each file"
)

parser.add_argument("filenames", nargs="+")
parser.add_argument("-l", "--lines", type=int, default=10)
args = parser.parse_args()  # 解析参数
print(args)
