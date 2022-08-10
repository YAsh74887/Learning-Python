
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bid={}

def find_highest_bid(bidding_record):
  highest_bid = 0
  winner = ""
  
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
      
  print(f"The winner is {winner} and the Highest Bid is {highest_bid}")


bidding_finished=False
while not bidding_finished: 
  name = input("What is your name? \n")
  price = int(input("Enter your bid: \n"))

  bid[name]=price
  
  should_continue = input("DO you want to continue if type YES or NO\n")
  if should_continue == "no":
    
    bidding_finished = True 
    find_highest_bid(bid)
  else:
    bidding_finished = False  