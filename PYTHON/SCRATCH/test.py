import datetime

# Calculates the Days Between Two Dates
def calculateDaysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates
    """
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    return abs(date2 - date1)

# Test for calculateDaysBetweenDates
def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = calculateDaysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()