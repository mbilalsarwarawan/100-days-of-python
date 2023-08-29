from art import logo
import os


def find_winner(bidderlist):
    highest_bid = 0
    winning_bidder = ""
    for bidder in bidder_list:
        if bidder['bid'] > highest_bid:
            highest_bid = bidder['bid']
            winning_bidder = bidder['name']

    print(f"The winner is {winning_bidder}")
    print(f"The bid is {highest_bid}")


print(logo)
run = "yes"
bidder_list = []
while run == "yes":
    name = input("Enter the name of the bidder\n")
    bid = int(input("Enter the amount you want to bid\n"))
    run = input("Is there anybody who want to bid? Type yes or no\n")
    bidder = {"name": name,
              "bid": bid, }
    bidder_list.append(bidder)
    os.system('cls')

find_winner(bidder_list)
