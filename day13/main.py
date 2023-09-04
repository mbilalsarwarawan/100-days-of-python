from game_data import data
print(len(data))


def game():
    i = 0
    game = True
    while game:
        print(
            f"Compare A: {data[i]['name']} , a {data[i]['description']},  a {data[i]['country']}")
        print(
            f"Compare B: {data[i+1]['name']} , a {data[i+1]['description']},  a {data[i+1]['country']}")
        decision = input("Decide A or B\n")
        followers_of_A = data[i]['follower_count']
        followers_of_B = data[i+1]['follower_count']
        print(f"{followers_of_A}M followers")
        print(f"{followers_of_B}M followers")
        if followers_of_A < followers_of_B and decision == "b":

            print("you have chosen right")
        elif followers_of_A > followers_of_B and decision == "a":

            print("You have chosen the right")
        else:
            print("You have chosen the wrong")
            break
        i += 1


game()
