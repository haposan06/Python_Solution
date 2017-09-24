import turtle

def draw_circle(dist):
    angie = setTurtle(shape = "arrow", color = "blue", speed = 99999)
    angie.dot(100)
##    angie.circle(dist,120)
    
def draw_flower(abc):
    # code for flower design
    abc.pu()
    abc.setpos(-200,0)
    abc.pd()

    for i in range(1,37):  
        abc.left(35)
        abc.forward(50)
        abc.right(35)
        abc.forward(50)
        abc.right(145)
        abc.forward(50)
        abc.right(35)
        abc.forward(50)
        abc.right(10)
    abc.seth(270)
    abc.forward(200)
def draw_square(brad):
    

    for x in range(0,4):
        
        brad.forward(100)
        brad.right(90)

def draw_triangle(potter):
    
    for x in range(0,3):
        potter.forward(100)
        potter.left(120)
    
def setTurtle(shape, color, speed):
    babyTurtle = turtle.Turtle()
    babyTurtle.shape(shape)
    babyTurtle.color(color)
    babyTurtle.speed(speed)
    return babyTurtle

def draw_everthing(length):
    window = turtle.Screen()
    window.bgcolor("Red")
    brad = setTurtle(shape = "turtle", color = "yellow", speed = 999999)
    draw_flower(brad)
    window.exitonclick()
    
draw_everthing(100)
