import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PONG")
screen.tracer(0)

class Scoreboard(turtle.Turtle):
  
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.update_score()
    
  def update_score(self): 
    self.clear() 
    self.goto(-60, 200)
    self.write(self.l_score, "center", font=("Courier", 60, "normal"))
    self.goto(60, 200)
    self.write(self.r_score, "center", font=("Courier", 60, "normal"))
    
  def l_point(self):
    self.l_score += 1
    self.update_score()
    
  def r_point(self):
    self.r_score += 1
    self.update_score()     
    
class Ball(turtle.Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    self.new_xcor = 10
    self.new_ycor = 10
    
  def move(self):
    
    new_x = self.xcor() + self.new_xcor
    new_y = self.ycor() + self.new_ycor
    self.goto(new_x, new_y)
      
  def bounce(self):
  
    self.new_ycor *= -1
    
  def bounce_for_paddle(self):
    
    self.new_xcor *= -1 
    
  def resetposition(self):
    self.goto(0, 0) 
    self.bounce_for_paddle()   
       
class Paddle(turtle.Turtle):
  def __init__(self,position):
    super().__init__()
    paddle = turtle.Turtle()
    self.shape("square")
    self.color("white")
    self.shapesize(5,1)
    self.penup()
    self.goto(position)
    

  def go_up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)
    
    
  def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)  
    
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
  
ball=Ball()
score = Scoreboard()
  
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
  X=0.1
  time.sleep(X)
  screen.update()
  ball.move()
  
  # collusion with ball
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce()
  
  # collusion with paddle 
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_for_paddle()
    X *= 0.9
    
  # detect when miss
  if ball.xcor() > 380:
    ball.resetposition() 
    score.l_point()
    
    
  if ball.xcor() < -380:  
    ball.resetposition()
    score.r_point() 
    
    

screen.exitonclick()