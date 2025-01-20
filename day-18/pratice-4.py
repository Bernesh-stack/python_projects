import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
import random
# import colorgram
#
#
# rgb_colors = []
#
# colors = colorgram.extract('colors.jpeg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colours = (r,g,b)
#     rgb_colors.append(colours)
# print(rgb_colors)


tim = Turtle()
sc = Screen()
tim.penup()
color_list = [(227, 227, 224), (225, 222, 224), (196, 173, 119), (216, 225, 219), (222, 225, 230), (162, 102, 57), (124, 36, 23), (185, 158, 52), (5, 53, 80), (47, 31, 28), (105, 68, 86), (113, 159, 174), (72, 36, 44), (22, 119, 168), (85, 137, 62), (8, 64, 44), (64, 152, 135), (130, 38, 42), (181, 97, 80), (208, 200, 148), (178, 201, 188), (147, 175, 160), (172, 153, 159), (214, 181, 175), (19, 78, 97), (96, 139, 151), (35, 77, 59), (212, 179, 183), (164, 200, 214), (148, 115, 122)]
tim.dot(20,random.choice(color_list))
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_dots = 100

for dot_count in range(1,number_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)










sc.exitonclick()