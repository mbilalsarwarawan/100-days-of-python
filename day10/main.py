import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def give_cards(number, cards):
    for _ in range(number):
        cards.append(deal_card())


def want_to_play():
    return input(
        "Do you want to deal more. \n if yes press 'y' or no press 'n'")


print(logo)
user_cards = []
computer_cards = []
give_cards(2, computer_cards)
give_cards(2, user_cards)


game_is_continue = True
winner = ""
while game_is_continue:
    print(f"You cards are {user_cards}")
    print(f"Computer cards are {computer_cards[:-1]}")

    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)

    if user_sum > 21:
        game_is_continue = False
        winner = "Dealer"
    elif user_sum == 21:
        game_is_continue = False
        winner = "You"

    elif user_sum < 21 and computer_sum >= 17:
        option = want_to_play()
        if option == "n":
            if computer_sum > 21:
                winner = "You"
                game_is_continue = False
            elif computer_sum == 21:
                winner = "Dealer"
                game_is_continue = False
            else:
                if computer_sum == user_sum:
                    winner = "Tie"
                elif computer_sum > user_sum:
                    winner = "Dealer"
                else:
                    winner = "You"
                game_is_continue = False
        else:
            give_cards(1, computer_cards)
            give_cards(1, user_cards)
    elif user_sum < 21 and computer_sum < 17:

        option = want_to_play()
        if option == "n":
            while sum(computer_cards) < 17:
                give_cards(1, computer_cards)

        game_is_continue = False
        if computer_sum == user_sum:
            winner = "Tie"
        elif computer_sum > user_sum:
            winner = "Dealer"
        else:
            winner = "You"

print(winner +
      f" is the winner\ncomputer final hand : {computer_cards}" + "\n"+f"You final hand :{user_cards}")
