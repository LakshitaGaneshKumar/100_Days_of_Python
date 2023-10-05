from blind_auction_art import logo
from replit import clear

#print logo
print(logo)

# initialize variables and dicts
more_bids = "yes"
bid_list = {}

#prompt user for name and bid while there are bidders
while more_bids == "yes":
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    #add name and bids to bid_list
    bid_list[name] = bid

    #prompt for more bidders
    more_bids = input('Are there any other bidders? Type "yes" or "no" ')
    if more_bids == "yes":
        clear()

#compute the highest bid
highest_bid = 0
for bidder in bid_list:
    if bid_list[bidder] > highest_bid:
        max_bidder = bidder
        max_bid = bid_list[bidder]

#print result
print(f"The winner is {max_bidder} with a bid of ${max_bid}")
