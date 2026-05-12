import turtle
from turtle import *

import math
import random

#ATTENTION!!! PLEASE CHANGE THE RESOLUTION OF THE SCREEN
#IF YOU ARE ON A LAPTOP
width = 1920
height = 1300
setup(width, height)

#screen = Screen() #REMOVE THE COMMENT HERE
#width = screen.window_width(), screen.window_height() #REMOVE THE COMMENT HERE
#screen.setworldcoordinates (-1600, -1083, 1600,1083 ) #REMOVE THE COMMENT HERE



# turn off animation, comment it out to see the drawing process #this as well from the cheatsheet
tracer(2)
bgcolor('white') #From cheatsheet
color('#000') # same here


pensize(4)
penup()
right(90)
forward(600)
left(90)
pendown()
forward(550)
left(125)


fillcolor('yellow')
begin_fill()

for i in range(63):
    forward(math.sqrt(i)*0.7)
    left(i%1.5)


right(150)


for i in range(170):
    forward(math.sqrt(i)*0.45)
    left(i%1.7)

right(188)
penup()
forward(100)
left(50)
pendown()
forward(130)

for i in range(45):
    forward(math.sqrt(i)*1.1)
    left(i%1.2)


for i in range(50):
    forward(math.sqrt(i)*0.5)
    left(i%1.3)

for i in range(50):
    forward(math.sqrt(i)*0.2)
    left(i%5)

for i in range(54):
    forward(math.sqrt(i)*2.1)
    left(i%1.58)

right(66)

for i in range(56):
    forward(math.sqrt(i)*2)
    left(i%2.57)


penup()
right(188)
forward(200)
pendown()
left(25)

for i in range(48):
    forward(math.sqrt(i)*0.8)
    left(i%1)

for i in range(45):
    forward(math.sqrt(i)*0.6)
    left(i%0.7)

for i in range(30):
    forward(math.sqrt(i)*0.7)
    left(i%2.6)

for i in range(10):
    forward(math.sqrt(i)*0.5)
    left(i%1.5)

for i in range(31):
    forward(math.sqrt(i)*0.5)
    left(i%7)

for i in range(60):
    forward(math.sqrt(i)*1.5)
    left(i%1.1)


for i in range(60):
    forward(math.sqrt(i)*1.5)
    left(i%1.1)


left(52)

for i in range(37):
    forward(math.sqrt(i)*2)

while True:
    for i in range(32):
        forward(math.sqrt(i)*1.5)
        right(i%1.4)

    right(165.5)
    penup()
    break

forward(466)


pendown()

left(1)
forward(29)

for i in range(20):
    forward(math.sqrt(i)*0.5)
    right(i%4.9)


forward(109)

for i in range(20):
    forward(math.sqrt(i)*0.5)
    left(i%10)

for i in range(25):
    forward(math.sqrt(i)*0.6)
    left(i%7)

forward(100)


right(105)

for i in range(64):
    forward(math.sqrt(i)*0.5)
    left(i%2)

for i in range(29):
    forward(math.sqrt(i)*0.5)
    left(i%10)

forward(90)

right(88)

forward(36)

for i in range(55):
    forward(math.sqrt(i)*0.5)
    left(i%4.6)


for i in range(20):
    forward(math.sqrt(i)*0.5)
    left(i%5)

forward(15)

for i in range(23):
    forward(math.sqrt(i)*0.5)
    left(i%10)

forward(37)

right(125)

for i in range(25):
    forward(math.sqrt(i)*0.5)
    left(i%2)

for i in range(29):
    forward(math.sqrt(i)*0.5)
    left(i%11)


right(120)

forward(100)
right(180)
forward(100)
right(148)
forward(100)
right(180)
forward(100)
right(90)

for i in range(33):
    forward(math.sqrt(i)*0.5)
    left(i%2)

for i in range(35):
    forward(math.sqrt(i)*0.5)
    left(i%6)

right(20)
forward(28)
penup()
left(88)
forward(140)
left(130)
forward(10)
right(140)
pendown()

for i in range(27):
    forward(math.sqrt(i)*3)
    left(i%3)


for i in range(39):
    forward(math.sqrt(i)*1.0)
    left(i%2)


for i in range(15):
    forward(math.sqrt(i)*1)
    left(i%3)

for i in range(20):
    forward(math.sqrt(i)*1.7)
    left(i%3)

right(0.4)
forward(850)
end_fill()





# move to the center
penup()
goto(0,0)
forward (235)
right(90)
forward(120)
left(90)
pendown()

fillcolor('black')
begin_fill()
circle(90,360,300)
end_fill()
penup()
left(90)
forward(180)
left(90)
pendown()
fillcolor('white')
begin_fill()
circle(44)
end_fill()
penup()
forward(530)
left(90)

pendown()
left(90)
forward(28)

fillcolor('black')
begin_fill()
for i in range(30):
    forward(math.sqrt(i)*1.5)
    right(i%6)

right(195)

for i in range(28):
    forward(math.sqrt(i)*1)
    left(i%4)

for i in range(15):
    forward(math.sqrt(i)*1.7)
    left(i%7)

for i in range(11):
    forward(math.sqrt(i)*2.4)
    left(i%11)
end_fill()

penup()
forward(210)
pendown()

right(110)
forward(10)

right(73)

pencolor('red')
fillcolor('red')
begin_fill()
for i in range(25):
    forward(math.sqrt(i)*1)
    right(i%2)

for i in range(15):
    forward(math.sqrt(i)*2)
    right(i%6)

for i in range(10):
    forward(math.sqrt(i)*2)
    right(i%8)


for i in range(42):
    forward(math.sqrt(i)*1.12)
    right(i%5)


for i in range(19):
    forward(math.sqrt(i)*1.54)
    right(i%5)
end_fill()


penup()

goto(0,0)
left(55)
forward(39)
right(90)
forward(63)
right(180)
pendown()
pencolor('black')


forward(30)
fillcolor('black')
begin_fill()
for i in range(7):
    forward(math.sqrt(i)*1.5)
    right(i%1.3)

right(60)

for i in range(30):
    forward(math.sqrt(i)*0.2)
    right(i%6)

for i in range(20):
    forward(math.sqrt(i)*0.2)
    right(i%6)

for i in range(15):
    forward(math.sqrt(i)*1.12)
    right(i%10)


end_fill()
penup()
left(120)
forward(120)
right(90)
forward(50)
right(180)

pendown()
fillcolor('black')
begin_fill()
for i in range(10):
    forward(math.sqrt(i)*1.5)
    right(i%1.5)

for i in range(30):
    forward(math.sqrt(i)*0.9)
    left(i%7)

for i in range(30):
    forward(math.sqrt(i)*0.9)
    right(i%8)


for i in range(30):
    forward(math.sqrt(i)*0.9)
    left(i%5)

for i in range(8):
    forward(math.sqrt(i)*0.8)
    left(i%8)

for i in range(10):
    forward(math.sqrt(i)*0.2)
    right(i%10)

for i in range(20):
    forward(math.sqrt(i)*0.2)
    right(i%10)

for i in range(20):
    forward(math.sqrt(i)*0.2)
    right(i%9)


for i in range(60):
    forward(math.sqrt(i)*0.3)
    right(i%2)


for i in range(38):
    forward(math.sqrt(i)*0.3)
    right(i%3)


for i in range(25):
    forward(math.sqrt(i)*0.4)
    left(i%7)

for i in range(20):
    forward(math.sqrt(i)*1)
    left(i%5)

for i in range(28):
    forward(math.sqrt(i)*1)
    right(i%8)

for i in range(26):
    forward(math.sqrt(i)*0.32)
    right(i%5)
end_fill()

penup()
forward(400)

goto(0,0)

right(90)
forward(200)
right(88)
forward(277)
pencolor('red')
pendown()
fillcolor('red')
begin_fill()
for i in range(13):
    forward(math.sqrt(i)*1)
    left(i%2)

for i in range(30):
    forward(math.sqrt(i)*1.5)
    left(i%6)

for i in range(30):
    forward(math.sqrt(i)*1.6)
    left(i%6)

for i in range(10):
    forward(math.sqrt(i)*1.2)
    left(i%2)

for i in range(17):
    forward(math.sqrt(i)*1.2)
    left(i%2)

for i in range(17):
    forward(math.sqrt(i)*1.2)
    left(i%6)

for i in range(40):
    forward(math.sqrt(i)*1.4)
    left(i%6)

for i in range(15):
    forward(math.sqrt(i)*1.8)
    left(i%5)

for i in range(11):
    forward(math.sqrt(i)*2)
    left(i%6)
forward(2)
end_fill()
penup()
goto(0,0)

left(86.73)

forward(606.5)

pencolor('black')
pendown()
fillcolor('black')
begin_fill()
for i in range(10):
    forward(math.sqrt(i)*2)
    left(i%10)

for i in range(10):
    forward(math.sqrt(i)*5.1)
    left(i%7)

for i in range(10):
    forward(math.sqrt(i)*5.7)
    left(i%9)

right(110)
for i in range(11):
    forward(math.sqrt(i)*6.4)
    right(i%3)

for i in range(10):
    forward(math.sqrt(i)*1)
    right(i%8)

for i in range(10):
    forward(math.sqrt(i)*1)
    right(i%8)

for i in range(10):
    forward(math.sqrt(i)*1)
    right(i%8)

for i in range(10):
    forward(math.sqrt(i)*1)
    right(i%7)

for i in range(10):
    forward(math.sqrt(i)*1)
    right(i%2)

for i in range(30):
    forward(math.sqrt(i)*1)
    right(i%3)

for i in range(19):
    forward(math.sqrt(i)*2)
    right(i%1)

for i in range(10):
    forward(math.sqrt(i)*1.2)
    right(i%4)
end_fill()
penup()

goto(0,0)

right(115)
forward(350)
left(50)
pendown()
fillcolor('black')
begin_fill()
for i in range(16):
    forward(math.sqrt(i)*5.48)
    left(i%8)
right(147)

for i in range(12):
    forward(math.sqrt(i)*8)
    right(i%4)

for i in range(10):
    forward(math.sqrt(i)*2.7)
    right(i%2)

for i in range(10):
    forward(math.sqrt(i)*2)
    right(i%10)

for i in range(19):
    forward(math.sqrt(i)*1.55)
    right(i%12)

for i in range(20):
    forward(math.sqrt(i)*2.8)
    right(i%2)
end_fill()

penup()
tracer(0)
goto(0,0)

star_colors = ['gold', 'orange', 'yellow','black']
star_color  = random.choice(star_colors)
star_height = random.randint(50,200)

penup()
goto(-650, 150)
setheading(72)
pencolor(star_color)
fillcolor(star_color)
pendown()
begin_fill()
for i in range(5):
    forward(star_height)
    right(144)
end_fill()
penup()


done()
