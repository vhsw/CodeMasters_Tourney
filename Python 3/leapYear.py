# Determine if a given year is leap or not.


def leapYear(year):
    return (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0
