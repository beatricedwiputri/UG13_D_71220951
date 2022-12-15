import turtle
t = turtle.Turtle()

turtle.Screen().bgcolor("purple")
t.pensize(10)
t.pencolor("white")

#huruf B
t.up()
t.goto(0,200)
t.down()
t.circle(50,180)
t.left(90)
t.forward(200)
t.left(90)
t.circle(50,180)


#5
t.up()
t.goto(50,30)
t.down()
t.forward(50)
t.left(90)
t.forward(75)
t.left(90)
t.up()
t.goto(0,-145)
t.down()
t.circle(50,180)


#huruf D
t.up()
t.goto(0,-210)
t.down()
t.left(90)
t.forward(175)
t.left(90)
t.circle(90,180)


#7
t.up()
t.goto(-225,30)
t.down()
t.right(180)
t.forward(75)
t.right(110)
t.forward(175)


#1
t.up()
t.goto(225,0)
t.down()
t.right(200)
t.forward(50)
t.right(140)
t.forward(175)


s = turtle.Screen().exitonclick()

