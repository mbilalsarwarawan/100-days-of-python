def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_year(year):
    """Takes a year gives the number of days in year and check its leap year than gives the answer accordingly"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 31]
    if leap_year(year):
        month_days[1] = 29
    total_days = sum(month_days)
    return total_days


print(days_in_year(2000))
