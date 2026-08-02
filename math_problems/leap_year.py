def leap_year(year: int) -> bool:
    """Leap Year.

    An extra day is added to the calendar almost every four years as February 29, and the day is called
    a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to
    orbit the sun. A leap year contains a leap day.

    In the Gregorian calendar, three conditions are used to identify leap years: the year can be evenly
    divided by 4, is a leap year, unless: the year can be evenly divided by 100, it is NOT a leap year,
    unless: the year is also evenly divisible by 400, then it is a leap year. This means that in the
    Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and
    2500 are NOT leap years.

    Task: given a year, determine whether it is a leap year. If it is a leap year, return the Boolean
    True, otherwise return False.

    Input Format: the year to test.

    Output Format: the function must return a Boolean value (True/False).
    """
    leap = False

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        else:
            leap = True
    else:
        leap = False

    return leap
