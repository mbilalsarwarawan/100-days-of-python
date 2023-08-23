import random

# dice = random.randint(0, 1)
# if dice == 0:
#     print("head")
# else:
#     print("tale")
names_string = input("Enter the names of the participants.\n")
names = names_string.split(", ")
print(names[random.randint(0, len(names)-1)])
