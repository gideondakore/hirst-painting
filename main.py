import turtle as t
import random

# import colorgram
# color = colorgram.extract("hirst_painting.jpg", 30)
#
# color_list = []
# for i in range(len(color) - 1):
#     f_color = color[i]
#     rgb = f_color.rgb
#     color_list.append(tuple(list(rgb)))
#
# print(color_list)

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
          (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138),
          (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151),
          (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120),
          (202, 185, 190), (40, 72, 82), (46, 73, 62)]


tim = t.Turtle()

t.colormode(255)


def teleport(x, y):
    tim.penup()
    tim.setpos(x, y)
    tim.pendown()


xcoord = -220.0
ycoord = -200.0

teleport(xcoord, ycoord)
tim.hideturtle()
tim.speed(10)
for i in range(10):
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.fd(50)
    ycoord = tim.ycor()
    tim.setpos(xcoord, ycoord+40)


screen = t.Screen()
screen.exitonclick()