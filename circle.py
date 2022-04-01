'''from turtle import*
bgcolor('black')
speed(30)
hideturtle()
for i in range(60):
   color('blue')
   circle(i)
   color('red')
   circle(i* 0.8) 
   left(3)
   backward(3)
for j in range(60):
   color('white')
   circle(j)
   color('yellow')
   circle(j* 0.4) 
   right(3)
   forward(3)
done()
'''

'''import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
col=['yellow','red','pinl','cyan','green','blue']
for i in range(120):
    t.pencolor(col[i%6])
    t.circle(190-i/2,90)
    t.lt(90)
    t.circle(190-i/3,90)
    t.lt(60)
    t.circle(180-i/4,90)
    t.lt(60)
    t.circle(180-i/5,90)
    t.lt(60)
    t.circle(180-i/6,90)
    t.lt(60)
s.exitclick()    
'''

from turtle import *
speed(10)
color ('cyan')
bgcolor('black')
b=200
while b>0:
    left(b)
    forward(b*3)
    b=b-1
    
