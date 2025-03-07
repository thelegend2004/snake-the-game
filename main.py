from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Ultra Snake Game 2000")

segments = []

for i in range(3):
    s = Turtle()
    s.shape("square")
    s.color("white")
    segments.append(s)

segments[1].goto(x=-20,y=0)
segments[2].goto(x=-40,y=0)

screen.exitonclick()