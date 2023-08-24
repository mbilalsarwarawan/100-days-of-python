# students_height = input("Input the list of the students height\n").split()

# for n in range(0, len(students_height)):
#     students_height[n] = int(students_height[n])
# average = 0
# for student in students_height:
#     average += student
# average /= len(students_height)
# print(average)
# total = 0
# for n in range(1, 101):
#     if n % 2 == 0:
#         total += n

# print(total)

for n in range(1, 100):
    if n % 3 == 0 and n % 5 == 0:
        print("fizz buzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
