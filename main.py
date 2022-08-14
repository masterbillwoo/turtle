# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import turtle as t


tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed(100)
for i in range(50):
    tim.color(random_color())
    tim.circle(100)
    tim.left(10)







"""tim = t.Turtle()
tim.shape("turtle")
#tim.color("purple")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
tim.color(random_color())
tim.forward(1000)
"""

"""def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.left(angle)

for i in range(3, 11):
    tim.pensize(10)
    draw_shape(i)"""

#draw a square
"""tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)"""

#draw a pengtagon
"""tim.forward(100)
tim.left(72)
tim.forward(100)
tim.left(72)
tim.forward(100)
tim.left(72)
tim.forward(100)
tim.left(72)
tim.forward(100)"""

#draw a dashed line
"""tim.forward(100)
tim.penup()
tim.forward(100)
tim.pendown()
tim.forward(100)"""



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
