import random
import turtle
import time


STARTING_POSTION  = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
  def __init__(self):
    self.segment = []
    self.create_snake() 
    
  def create_snake(self):
    for i in STARTING_POSTION:
      self.add_segment(i)
      
  def add_segment(self,i):
    timmy = turtle.Turtle()
    timmy.speed(1)
    timmy.shape("square")
    timmy.color("white")
    timmy.penup()
    timmy.goto(i)
    self.segment.append(timmy)
    
    
  def extend(self):
    self.add_segment(self.segment[-1].position())
        
  def move(self):
      for seg in range(len(self.segment)-1, 0, -1):
        new_x = self.segment[seg-1].xcor()
        new_y = self.segment[seg-1].ycor()
        self.segment[seg].goto(new_x, new_y)
     
      self.segment[0].forward(MOVE_DISTANCE)   
      
      
  def up(self):
    if self.segment[0].heading() != 270:
      self.segment[0].setheading(90)   
    
  def left(self):
    if self.segment[0].heading() != 0:
      self.segment[0].setheading(180)   
    
  def down(self):
    if self.segment[0].heading() != 90:
      self.segment[0].setheading(270)   
      
  def right(self):
    if self.segment[0].heading() != 180:
      self.segment[0].setheading(0) 
       
      
class Food(turtle.Turtle):
  def __init__(self):
    super().__init__()   
    self.shape("circle")
    self.penup()
    self.shapesize(0.5, 0.5)  
    self.color("red")
    self.speed("fastest")
    self.refresh()       

    
  def refresh(self):
    rand_x = random.randint(-200,200)
    rand_y = random.randint(-200,200)
    self.goto(rand_x, rand_y)  
    
    
class Scoreboard(turtle.Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.color("white")
    self.goto(0,260)
    self.score = 0
    self.write(f"Score: {self.score}", align="center", font=("Arial", "22", "normal"))
    self.hideturtle()
   
    
    
  def increasescore(self):
    self.score += 1
    self.clear()
    self.write(f"Score: {self.score}", align="center", font=("Arial", "22", "normal"))
    
    
  def gameover(self):
    self.goto(0,0)
    self.write(f"GAME OVER. ", align="center", font=("Arial", "22", "normal"))  
     

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")


s = Scoreboard()

game = True
while  game:
  score = 0
  screen.update()
  time.sleep(0.1)
  snake.move()
  
  # collusion with food 
  if snake.segment[0].distance(food) < 15:
    s.increasescore()
    snake.extend()
    food.refresh()
    
    
  #collusion with wall
  wall = 295
  head = snake.segment[0]
  if head.xcor() > wall or head.xcor() < -wall or head.ycor() > wall or head.ycor() < -wall:
    game = False
    s.gameover()
    
  #collusion with snake 
  for segment in snake.segment[1:]:

    if snake.segment[0].distance(segment) < 10:
      game = False 
      s.gameover()
      
    
 
    

turtle.exitonclick()
