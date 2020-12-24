# 圖形一:畫出幾何圖案，畫出一排彩色正方形
# (1)準備工作(色彩)
import turtle
shelly = turtle.Turtle()
turtle.bgcolor("black")

# (2)劃出6個正方形，個差30步
for n in range(6):
    colors = ["red","green","blue","gold","purple","yellow"]
    shelly.color(colors[n])
    for i in range(4):
        shelly.forward(25)
        shelly.left(90)
    shelly.penup
    shelly.forward(30)
    shelly.pendown()
# (3)隱藏海龜
shelly.hideturtle()
