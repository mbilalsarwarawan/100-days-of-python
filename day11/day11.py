import random
from arts import logo


def guess_number(mode):

    number = random.randint(1, 100)
    if mode == "easy":
        tries = 10
    else:
        tries = 5
    while tries > 0:
        print(f"You have {tries} attempts remaining to guess a number.")
        guessed = int(input("Make a guess :"))
        if guessed < number:
            print("Too low")
        elif guessed > number:
            print("Too high")
        else:
            print("You win! guessed the right number")
            break

        tries -= 1
    if (tries <= 0):
        print("You are out of attempts.! you lose")


print(logo)
print("Welcome to the game in guessing a number")
mode = input("Choose a difficulty level : Type easy or hard\n")
guess_number(mode)
