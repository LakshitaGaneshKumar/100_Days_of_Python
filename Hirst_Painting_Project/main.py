# #######################################################
# ## EXTRACT COLORS FROM IMAGE ###
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# #######################################################
import turtle as t
import random

t.colormode(255)
colors = ["royal blue", "slate blue", "medium aquamarine", "cornflower blue", "sea green", "light steel blue", (229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85)]
tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.setpos(-300, -200)
tim.speed("fastest")

for j in range(10):
    for i in range(10):
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.fd(50)
    tim.setpos(-300, -200 + ((j + 1) * 50))

screen = t.Screen()
screen.exitonclick()
