import random
from turtle import Turtle , Screen 

timmy = Turtle()
timmy.shape()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy.width(5)
timmy.speed(0)


for i in range(36):
  timmy.color(random.choice(colours))
  timmy.circle(100)
  timmy.left(10)


screen = Screen()
screen.exitonclick()