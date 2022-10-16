import time
from turtle import Screen, Turtle
import turtle
import random
from venv import create

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

FONT = ("Courier", 24, "normal")

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


class Player(turtle.Turtle):
  def __init__(self):
     super().__init__()
     self.color("black")
     self.shape("turtle")
     self.penup()
     self.goto(STARTING_POSITION)
     self.setheading(90)
     
  def Up(self):
    y = self.ycor() + MOVE_DISTANCE
    self.goto(0,y)
    
class CarManager:
  def __init__(self):
    self.all_cars = [] 
    self.car_speed = STARTING_MOVE_DISTANCE
    
  def create_car(self):  
    randomchance = random.randint(1,10)
    if randomchance == 1:
      new_cars = Turtle() 
      new_cars.shape("square")
      new_cars.shapesize(1,2)
      new_cars.penup()
      new_cars.color(random.choice(COLORS))
      y = random.randint(-250, 250)
      new_cars.goto(280, y)
      self.all_cars.append(new_cars)
     
  def move(self):
    for car in self.all_cars:
      car.backward(self.car_speed)
      
  def level_up(self):
    self.car_speed += STARTING_MOVE_DISTANCE      

class Scoreboard(turtle.Turtle):
    def __init__(self):
      super().__init__()
      self.level = 1
      self.hideturtle()
      self.penup()
      self.update()
      
    def update(self):
      self.clear()
      self.goto(-280,260)
      self.write(f"LEVEL:{self.level}", "center", font=("Courier", 15, "normal"))
        
      
    def increase_level(self):
      self.level+=1 
      self.update() 
      
    
s =Scoreboard()   
carmanager = CarManager()
player = Player()

screen.listen()
screen.onkey(player.Up,"Up")
screen.onkey(player.Up,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move()
    
    for car in carmanager.all_cars:
      if car.distance(player) < 28:
        turtle.write("GAME OVER" ,align='CENTER',font=('Arial',15,'bold'))
        game_is_on = False
    
        
    if player.ycor() > FINISH_LINE_Y:
      player.goto(STARTING_POSITION)  
      carmanager.level_up()
      s.increase_level()
   
   
screen.exitonclick()   
 
   
