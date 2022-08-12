logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# add
def add (n1, n2):
  return n1+n2

# sub
def sub (n1, n2):
  return n1-n2

# multi
def multi (n1, n2):
  return n1*n2

# div
def div (n1, n2):
  return n1/n2

operation={
  "+": add,
  "-": sub,
  "*": multi,
  "/": div
}
print(logo)
# function 

n1=float(input("What is the first no. \n"))
for op in operation:
  print(op)


loop = False 
while not loop:
  operation_symbol = input("Pick any symbol from above \n")  
  n2=float(input("What is the second no. \n"))
  calculation_fun=operation[operation_symbol]
  answer = calculation_fun(n1,n2)
  print(f"{n1} {operation_symbol} {n2} = {answer}")
     
     
  user = input("Enter Y or N, Y for continue and N for exit \n").lower()  
  if user == "y":
    n1 = answer
      
  else:
    loop = True
        

       
   
  

  