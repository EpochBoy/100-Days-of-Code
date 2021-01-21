from art import logo
import os

print(logo)

#create dict where name is key and bid is value
state = ""
bidders = {}

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_bidder():
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bidders[name] = bid
    state = input("Are there any other bidders? ")
    if state == "yes":
        cls()
        runner(state)
    else:
        runner(state)

def find_winner():
    for i in bidders:
        for j in bidders:
            if bidders[j] > bidders[i]:
                global winner_name
                winner_name = j
                global winning_amount
                winning_amount = bidders[j]

def runner(state):
    if state == "no":
        find_winner()
        print(f"Winner is {winner_name} and he won with a bid of {winning_amount}")
    else:
        get_bidder()

runner(state)


#Facit below

# from replit import clear
# from art import logo
# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()
  