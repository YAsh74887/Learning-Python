# -*- coding: utf-8 -*-
"""roller_coaster_ticket_calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1noHPLhNjDNMoKqGdW0k_HuaDsIwKPqNJ
"""

# inputing height from user 
height=int(input("Enter your height: "))
if height >= 120:
  bill = 0 
  print("You can enter the ride")
  age = int(input("What is your age: ")) 
  if age >= 18:
    bill = bill + 12
  if age <= 12:
    bill = bill + 5
  if age > 12 and age < 18:
    bill = bill + 7

  new_bill=bill
  # importing if user wants photos or not
  photos=input("Do you want Photos, Y or N:\n")

  if photos == "Y":
    new_bill = new_bill + 3
    print(f"The total bill is {new_bill}")

  else:
    print(f"The total bill is {new_bill}")       

else: 
  print("You can't enter the ride")

