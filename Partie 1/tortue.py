import turtle

t = turtle.Turtle()
''' 
t.forward(100)
t.left(90)
t.forward(50)
t.backward(100)
t.right(45)
t.forward(200) '''

# 5 marches d'escalier de 30 pixels

for i in range(1, 6):
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)


turtle.done()