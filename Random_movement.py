import random
from turtle import Turtle , Screen
import turtle 

timmy = Turtle()
timmy.shape()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [90, 180, 270, 360]
forward = [10, 50, 100]
timmy.width(10)
timmy.speed(1)
  

for i in range (200):
  timmy.color(random.choice(colours))
  timmy.fd(random.choice(forward))
  timmy.setheading(random.choice(directions))

















screen = Screen()
screen.exitonclick()