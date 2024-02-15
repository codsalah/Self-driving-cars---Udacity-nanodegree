# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.


def isLeapYear(year):
    """Returns True if the given year is a leap year, otherwise False."""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
def daysInmonth(year, month):
    if (month == 1) or (month == 3) or (month == 5) or (month == 7)\
          or (month == 8) or (month == 10) or (month == 12):
        return 31
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 30

def nextDay(year, month, day):
    """Return the year, month, and day of the next day."""
    if day < daysInmonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1 and 
    year2/month2/day2. Assumes inputs are valid dates in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert dateIsBefore(year1, month1, day1, year2, month2, day2), "Invalid input: First date is not before the second date."
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    assert daysBetweenDates(2024,2,2,2024,2,3) == 1
    assert daysBetweenDates(2024,2,1,2024,2,2) == 1 
    assert nextDay(2024,6,6) == (2024,6,7) 
    assert nextDay(2024,4,30) == (2024,5,1) 
    assert nextDay(2024,12,31) == (2025,1,1) 

test()
print(daysBetweenDates(2024,2,1,2025,2,1))