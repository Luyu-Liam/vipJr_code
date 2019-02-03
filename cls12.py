
"""
def taiyi(radius, color1, color2):
    t.color('black', color1)
    t.begin_fill()
    t.circle(radius/2, 180)
    t.circle(radius, 180)
    t.left(180)
    t.circle(-radius/2, 180)
    t.end_fill()

    t.left(90)
    t.penup()
    t.fd(radius*0.35)
    t.right(90)
    t.down()
    t.color(color1, color2)

    t.begin_fill()
    t.circle(radius*0.15)
    t.end_fill()

    t.left(90)
    t.up()
    t.bk(radius*0.35)
    t.down()
    t.left(90)
def Main():
    taiyi(200, 'black', 'white')
    taiyi(200, 'white', 'black')



import turtle
t = turtle.Pen()
Main()
t.mainloop()
"""
salary = [25, 50, 50, 12.5, 12.5, 50, 12.5]
salary = sum(salary)
print(salary)
