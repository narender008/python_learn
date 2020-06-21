
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_this_leapyear(year):
    """ this is leap year varification """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """return numer of days in that year"""
    if not 1 <= month <= 12:
        return "invalid month"

    if month == 2 and is_this_leapyear(year):
        return 29

    return month_days[month]


print(is_this_leapyear(2020))
