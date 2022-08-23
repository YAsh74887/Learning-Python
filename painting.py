import random
from turtle import Turtle , Screen 

timmy = Turtle()
timmy.shape()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


n=2
stop = False
while  not stop:
   n+= 1
   for i in range (n):
      timmy.color(random.choice(colours))
      timmy.fd(50)
      timmy.right(360/n)
     
   if n == 10:
      stop = True   


screen = Screen()
screen.exitonclick()