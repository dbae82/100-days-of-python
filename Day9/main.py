import os
from art import logo


def clear(): return os.system('clear')


print(logo)

auction = {}
more_bids = True
highest_bidder = ""
winning_bid = 0

while more_bids:
    name = input("What is your name?\n")
    bid = int(input("What is Your bid?\n$"))

    auction[name] = bid

    another_bid = input("Are there any other bids? 'Yes' or 'No'?\n").lower()

    if another_bid == "yes":
        clear()
    else:
        more_bids = False

for person in auction:
    if auction[person] > winning_bid:
        highest_bidder = person
        winning_bid = auction[person]

print(f"The winner is {highest_bidder} with a bid of ${winning_bid}.")
