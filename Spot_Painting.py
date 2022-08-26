import random
from turtle import Turtle , Screen

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy = Turtle() 
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.fd(300)
timmy.setheading(0)
timmy.speed(0)


 
 
i = 100 
for i in range(1, 101):

    
    timmy.dot(20, random.choice(colours))
    timmy.fd(50)
    
    
    if i % 10 == 0:
      timmy.setheading(90)
      timmy.forward(50)
      timmy.setheading(180)    
      timmy.forward(500)  
      timmy.setheading(0) 

  
 

   







screen = Screen()
screen.exitonclick()
