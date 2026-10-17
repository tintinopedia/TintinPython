import turtle
t=turtle.Turtle()
t.pensize(5)
t.color("Purple","Red")
t.begin_fill()
for i in range(4):
    t.forward(90)
    t.right(90)
t.end_fill()