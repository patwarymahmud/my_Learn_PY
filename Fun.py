# import turtle as t
# t.speed(0)
# t.bgcolor("black")
# t.color("aqua")
# t.hideturtle()
# for i in range(170):
#   t.circle(i)
#   t.left(5)
# t.done()

# from turtle import *
# speed(0)
# bgcolor("black")
# colors = ['orange', 'aqua']
# hideturtle()
# for i in range(122):
#   goto(0, 0)
#   color(colors[i % 2])
#   forward(130)
#   left(3)
#   circle(40)
#   forward(130)
#   right(90)
# done()

 from colorsys import *
 setpos(0, 80)
 speed(0)
 bgcolor("black")
 pensize(2)
 h = 0.71
 for i in range(150):
   c = hsv_to_rgb(h, 1, 1)
   color(c)
   h += 0.004
   circle(140 - 1, 90)
   lt(90)
   lt(20)
   circle(140 - 1, 90)
   lt(18)
 hideturtle()
 done()

# import turtle as t
# import colorsys
# t.bgcolor("black")
# t.tracer(100)
# t.pensize(1)
# h = 0.5
# for i in range(250):
#   c = colorsys.hsv_to_rgb(h, 1, 1)
#   h = 0.0008
#   t.fillcolor(c)
#   t.begin_fill()
#   t.fd(i)
#   t.lt(100)
#   t.circle(30)
#   for j in range(2):
#     t.fd(i*j)
#     t.rt(109)
#     t.end_fill()
