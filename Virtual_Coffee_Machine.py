
def report (water_in_mc, milk_in_mc, coffee_in_mc, money):
  print(f"Water: {water_in_mc}ml\nMilk: {milk_in_mc}ml\nCoffee: {coffee_in_mc}g\nMoney: {money}$")
  
  
def used_water(water_in_mc, water):
  water_in_mc = water_in_mc - water
  return water_in_mc

def used_milk(milk_in_mc, milk):
  milk_in_mc = milk_in_mc - milk
  return milk_in_mc

def used_coffee(coffee_in_mc, coffee):
  coffee_in_mc = coffee_in_mc - coffee
  return coffee_in_mc 


def less_resources(water_in_mc, water, milk_in_mc, milk, coffee_in_mc, coffee):
  if water_in_mc < water:
    print("Sorry there is not water left in machine")
    return ("no")
  elif milk_in_mc < milk:
    print("Sorry there is not milk left in machine")
    return ("no")
    
  elif coffee_in_mc < coffee:
    print("Sorry there is not coffee left in machine") 
    return ("no")
    
def money_input(user_money, cost, money):
  ''' money input in machine '''
  if user_money > cost:

    refund = user_money - cost
    money = refund
    print(f"Here is your extra money: {refund}")
    print(f"Enjoy your {user} ☕")
    return money
    
  elif user_money < cost:
    refund = cost - user_money
    print(f"Here is short fall of  money: {refund}")
    
  else:
      print("Enjoy your coffee")    


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1300,
    "milk": 1200,
    "coffee": 600,
}

money = 0

water_in_mc=resources['water']
milk_in_mc=resources['milk']
coffee_in_mc=resources['coffee']



off_the_mc = False 
while not off_the_mc:
  
  user = input("What would you like? (espresso/latte/cappuccino):\n").lower()
  if user == "report":
    report(water_in_mc, milk_in_mc, coffee_in_mc, money)
    off_the_mc = False
    
  elif user == "off":
    off_the_mc = True 

  elif user == "espresso" or "latte" or "cappuccino":
    water = MENU[user]['ingredients']['water']
    milk = MENU[user]['ingredients']['milk']  
    coffee = MENU[user]['ingredients']['coffee']  
    cost = MENU[user]['cost']


    user_money = int(input("Enter your money\n"))
    
    money += cost


    water_in_mc=(used_water(water_in_mc, water))
    milk_in_mc=(used_milk(milk_in_mc, milk))
    coffee_in_mc=(used_coffee(coffee_in_mc, coffee))
    
    money_input(user_money, cost, money)  
    
        
        
    if less_resources(water_in_mc, water, milk_in_mc, milk, coffee_in_mc, coffee)  == "no":
      off_the_mc = True  
    
  
  
   
    




