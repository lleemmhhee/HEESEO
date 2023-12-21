import turtle as tt
import random

def screenLeftClick(x,y):
    global r, g, b
    tt.pencolor((r, g, b))
    tt.pendown()
    tt.goto(x,y)

def screenRightClick(x,y):
    tt.penup()
    tt.goto(x,y)

def screenMidClick(x,y):
    global r, g, b
    tSize = random.randrange(1,10)
    tt.shapesize(tSize)
    r= random.random()
    g= random.random()
    b= random.random()

pSize=10
r, g, b = 0.0, 0.0, 0.0

tt.title('거북이로 그림 그리기')
tt.shape('turtle')
tt.pensize(pSize)

tt.onscreenclick(screenLeftClick, 1)
tt.onscreenclick(screenRightClick, 2)
tt.onscreenclick(screenMidClick, 3)

turtle.done()
    
