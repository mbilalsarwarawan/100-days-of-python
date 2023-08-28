def prime_checker(number):
    i = 2
    if number == 2 or number == 1:
        return True
    elif number <= 0:
        return False
    else:
        while number % i != 0:
            i = i+1
            if i == number:
                return True

        return False


for x in range(0, 100):
    print(prime_checker(x))
