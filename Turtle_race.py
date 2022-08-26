import random
import turtle

def random_colors():
  '''Generating random colours '''
  new_colors = random.choice(colours)
  colours.remove(new_colors)
  
  return new_colors

screen = turtle.Screen()

colours = ["blue", "yellow", "red", "green", "brown", "black"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter colour")

y=[150,100,50,0,-50,-100]
def position():
  new_positon = random.choice(y)
  y.remove(new_positon)
  
  return new_positon

all_turtle = []
for i in range(1,7):
  timmy = turtle.Turtle("turtle")
  timmy.penup()
  timmy.goto(-330,position())
  timmy.color(random_colors())
  all_turtle.append(timmy)


if user_bet:
  is_race_on  =  True 
  
  
while is_race_on:
  for turtle in all_turtle:
    
    if turtle.xcor() > 300:
      is_race_on = False
      winning_color = turtle.pencolor() 
      if winning_color == user_bet:
        print(f"You've won the race {winning_color} turtle is winner")
        
      else:
        print(f"You lose the game. The winner is {winning_color} the winner !!")   
        
    rand_dist = random.randint(0,10)
    turtle.forward(rand_dist)    
        
screen.exitonclick()
