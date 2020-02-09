def countingSundays():
    year = 1901
    month = 1
    # 1 = monday, 2 = tuesday, 3 = wednesday, 4 = thursday, 5 = friday, 6 = saturday, 7 = sunday
    dayofweek = 2
    sundaycount = 0
    while year != 2001:
        if dayofweek == 7:
            sundaycount += 1
            year, month, dayofweek = movetonextmonth(year, month, dayofweek)
        else:
            year, month, dayofweek = movetonextmonth(year, month, dayofweek)
    return sundaycount


def movetonextmonth(year, month, dayofweek):
    if month == 1:
        for i in [1] * 31:
            dayofweek += i
            if dayofweek == 8:
                dayofweek = 1
        month += 1

    elif month == 2:
        if year % 4 == 0:
            for i in [1] * 29:
                dayofweek += i
                if dayofweek == 8:
                    dayofweek = 1
        else:
            for i in [1] * 28:
                dayofweek += i
                if dayofweek == 8:
                    dayofweek = 1
        month += 1

    elif month == 3:
        for i in [1] * 31:
            dayofweek += i
            if dayofweek == 8:
                dayofweek = 1
        month += 1

    elif month == 4:
        for i in [1] * 30:
            dayofweek += i
            if dayofweek == 8:
                dayofweek = 1
        month += 1

    elif month == 5:
        for i in [1] * 31:
            dayofweek += i
            if dayofweek == 8:
                dayofweek = 1
        month += 1

    elif month == 6:
        for i in [1] * 30:
            dayofweek += i
            if dayofweek == 8:
                dayofweek = 1
        month += 1

    elif month == 7:
        for i in [1] * 31:
            dayofweek += i
            if dayofweek == 8:
                dayofweek = 1
        month += 1

    elif month == 8:
        for i in [1] * 31:
            dayofweek += i
            if dayofweek == 8:
                dayofweek = 1
        month += 1

    elif month == 9:
        for i in [1] * 30:
            dayofweek += i
            if dayofweek == 8:
                dayofweek = 1
        month += 1

    elif month == 10:
        for i in [1] * 31:
            dayofweek += i
            if dayofweek == 8:
                dayofweek = 1
        month += 1

    elif month == 11:
        for i in [1] * 30:
            dayofweek += i
            if dayofweek == 8:
                dayofweek = 1
        month += 1

    elif month == 12:
        for i in [1] * 31:
            dayofweek += i
            if dayofweek == 8:
                dayofweek = 1
        month = 1
        year += 1
    return year, month, dayofweek
print(countingSundays())
