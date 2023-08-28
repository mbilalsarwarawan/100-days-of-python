import math


def paint_calc(height, width, coverage):
    number_of_cans = (height*width)/coverage
    number_of_cans = math.ceil(number_of_cans)
    return number_of_cans


print(paint_calc(height=3, width=9, coverage=5))
