from replit import clear
# Hint: You can clear() to clear the otput in the console.abs

from art import logo
print(logo)

bids = {}
bidding_finished = False

# finding the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount =bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with  bid of  ${highest_bid}")

while not bidding_finished: 
    print("Welcome to the Secret Auction Program")
    name = input("What is your name?/n")
    price = input("what's yor bid? $ /n")
    bids =  [name] = price 
answer = input("Are there any other bidders?Type 'yes' or 'no'./n")
if  answer == "no":
    bidding_finished = True
    find_highest_bidder(bids)
elif answer == "yes":
    clear()
  
    