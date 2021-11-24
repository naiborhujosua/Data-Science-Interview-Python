# Draw Hirst Painting using Turtle
![Hirst Painting](https://github.com/naiborhujosua/100daysOfPythonCode/blob/main/hirst_painting/hirst_painting.gif)
import random
t.colormode(255)
tim = t.Turtle()
color_list = [(245, 238, 238), (248, 244, 244), (237, 246, 246), (201, 112, 112), (238, 241, 241), (152, 49, 49), (221, 138, 138), (171, 42, 42), (56, 126, 126), (139, 19, 19), (134, 184, 184), (197, 73, 73), (48, 88, 88), (98, 77, 77), (142, 148, 148), (75, 33, 33), (165, 156, 156), (15, 71, 71), (234, 164, 164), (54, 47, 47), (32, 77, 77), (145, 25, 25), (21, 89, 89), (182, 175, 175), (85, 127, 127), (44, 87, 87), (178, 98, 98), (222, 184, 184), (8, 51, 51), (108, 151, 151)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 ==0 :
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen =t.Screen()
screen.exitonclick()



