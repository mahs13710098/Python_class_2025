import turtle
turtle.getscreen()
t=turtle.Turtle()
for j in range(20):
    if j==0:
        for i in range(5):
            t.forward(100)
            t.right(72)
    else:
        t.right(18)
        for i in range(5):
            t.forward(100*((0.9)**j))
            t.right(72)





