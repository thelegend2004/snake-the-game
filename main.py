import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Ultra Snake Game 2000")
screen.tracer(0)

segments = []

for i in range(3):
    seg = Turtle()
    seg.shape("square")
    seg.color("white")
    seg.penup()
    seg.goto(x=(i*-20),y=0)
    segments.append(seg)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()