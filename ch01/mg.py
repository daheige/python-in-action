# 帮我生成一个玫瑰花的python脚本
# 创建画布和画笔
# 依赖 python-tk 组件库
import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

# 设置画笔属性
pen.color("red")
pen.fillcolor("pink")
pen.speed(0)

# 绘制玫瑰花
pen.begin_fill()
for _ in range(36):
    pen.forward(100)
    pen.right(100)
    pen.forward(100)
    pen.right(100)
pen.end_fill()

# 隐藏画笔
pen.hideturtle()

# 保持窗口打开
screen.exitonclick()
