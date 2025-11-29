import turtle


screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Дом БИШ СМОКА")
t = turtle.Turtle()

t.speed(2)
t.penup()


t.goto(-250, 250) 
t.pendown()


t.color("gold", "yellow")  
t.begin_fill()
t.circle(40)  
t.end_fill()
t.penup()




t.goto(-400, -500)
t.color("green")
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(800)
    t.left(90)
    t.forward(300)
    t.left(90)
t.end_fill()

t.penup()
t.color("dark red") 
t.goto(200, -200)
t.pendown()
t.begin_fill()
for i in range(3):
    t.left(90)
    t.forward(200)
t.end_fill()
t.penup()
t.goto(140, -150) 
t.color("cyan")
t.pendown()
t.begin_fill()
for i in range(4):
    t.left(90)
    t.forward(50)
t.end_fill()
t.penup()
t.goto(2, -6)
t.color("brown") 
t.left(140)
t.pendown()
t.begin_fill()
t.forward(150)
t.left(260)
t.forward(150)
t.end_fill()
t.penup()

t.goto(59,-199)
t.color("#c45210") 
t.right(220)
t.pendown()
t.begin_fill()
t.forward(80)
t.left(90)
t.forward(50)
t.left(90)
t.forward(80)
t.end_fill()
t.penup()

t.color("Yellow")
t.goto(15, -170)
t.pendown()
t.begin_fill()
t.circle(7)
t.penup()
t.end_fill()

t.color("#0095ff")
t.goto(-300, -203)
t.left(180)
t.right(20)
t.pendown()
t.begin_fill()
t.forward(369)
t.right(140)
t.forward(200)
t.left(140)
t.forward(150)
t.right(140)
t.forward(150)
t.right(20)
t.forward(160)
t.end_fill()
t.penup()

t.color("Brown")
t.goto(-250, -203)
t.pendown()
t.begin_fill()
t.left(180)
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(100)
t.end_fill()
t.penup()

t.color("Green")
t.goto(-312, -100)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

t.hideturtle()








turtle.exitonclick()

