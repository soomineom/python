from turtle import *
import turtle

inStr = ''
swidth,sheight = 500,500
tX,tY,tAngle,tSize = [0] * 4

turtle.title('거북 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width = swidth+50, height = sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.speed(5)

inStr = getString()

for ch in inStr:
    tX,tY,tAngle,tSize = getXYAS(swidth,sheight)
    r,g,b = getRGB()

    turtle.goto(tX,tY)
    turtle.left(tAngle)

    turtle.pencolor((r,g,b))
    turtle.write(ch, font = ('맑은고딕', tSize, 'bold'))

turtle.done()