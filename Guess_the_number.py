import random
print("GUESS THE NUMBER GAME ")
print(" I am thinking of a number between 1 and 100 \n Please guess")
print("Choose your difficulty level. Type EASY or HARD")
choose = input().lower()


numbers_list = []
def numbers():
  for i in range(1,101):
    numbers_list.append(i)
  
numbers()  
random_number = random.choice(numbers_list)


if choose == "hard":
  lives = 5
elif choose == "easy":
  lives = 10

  
is_game_complete = False
  
while  not is_game_complete:
  user_guess = int(input("Make your choice: \n")) 
  if lives == 1:
    print("YOU LOSE")
    is_game_complete = True

    
  elif user_guess > random_number:
    print("Your Guess is too High ")
    lives -= 1
    print(f"Your lives remaining : {lives}")
      
  elif user_guess < random_number:
    print("Your Guess is too low  ")
    lives -= 1
    print(f"Your lives remaining : {lives}")

    
  elif user_guess == random_number:
    print("Congratutaion You WIN") 
    is_game_complete = True  
    lives = 0 