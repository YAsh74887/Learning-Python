# -*- coding: utf-8 -*-
"""Rock_paper_scissors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iXDg4mzXImanuLJloZu28lTaij1Kp2m9
"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

list=0,1,2
computer=random.choice(list)
print(f"computer choice: {computer}")

if user <=2:

  # rock
  if user == 0:
    if computer == 1:
      print(f"user = {rock}\n CPU = {paper}")
      print("YOU LOSE")

    elif user == computer:
      # print(f"user = {rock}\n CPU = {paper}")
      print("TIE")

    elif computer == 2:
      print(f"user = {paper}\n CPU = {scissors}")
      print("YOU LOSE")


  # paper 

  if user == 1:
    if computer == 0:
      print(f"user = {paper}\n CPU = {rock}")
      print("YOU WIN") 

    elif computer == user:
      print("TIE")


    elif computer == 2:
      print(f"user = {paper}\n CPU = {scissors}")
      print("YOU LOSE")  


  # scissors 

  if user == 2:
    if computer == 0:
      print(f"user = {scissors}\n CPU = {rock}")
      print("YOU LOSE") 

    elif computer == user:
      print("TIE")


    elif computer == 1:
      print(f"user = {scissors}\n CPU = {paper}")
      print("YOU WIN")


else:
  print("Invaild syntax you lose")