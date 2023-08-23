import random

options = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
user_choice = int(input(
    "What do you want to choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
print(options[user_choice])
computer_choice = random.randint(0, 2)
print("Computer choses \n")
print(options[computer_choice])
if user_choice == computer_choice:
    print("Its a tie")
else:
    if user_choice == computer_choice+1:
        print("You win")
    else:
        print("You lose")
