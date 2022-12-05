
def add_time(start, duration, day = ''):
    #  setting up the new time
    start, duration = start.split(':'), duration.split(':')
    timeperiod = start[1][-2:]
    start[1] = start[1][0:2]

    #  converting the strings to ints to
    start, duration = [int(i) for i in start], [int(i) for i in duration]
    start[0], start[1] = start[0] + duration[0], start[1] + duration[1]

    #  adding to hours if the minutes count is over 60
    if start[1] // 60 != 0:
        start[0] += 1 * start[1] // 60
        start[1] = start[1] % 60
    if len(str(start[1])) == 1:
        if start[1] == 0:
            start[1] = '00'
        else:
            start[1] = '0' + str(start[1])
    start[1] = str(start[1])

    #  changing AM/PM
    switches = (start[0] // 12)
    dayspassed = 0  # if the time period switches from PM to AM, a day has passed
    for i in range(0, switches):
        if timeperiod == 'AM':
            timeperiod = 'PM'
        else:
            timeperiod = 'AM'
            dayspassed += 1
    #  days passed
    if len(day) > 0:
        daysoftheweek = {'sunday': 1, 'monday': 2, 'tuesday': 3, 'wednesday': 4,
                     'thursday': 5, 'friday': 6, 'saturday': 7}
        day = daysoftheweek[day.lower()]
        day += dayspassed
        if day > 7:
            temp = day // 7
            day = (7 * (temp+1)) - day
            if day > 0:
                day = 7 - day
            else:
                day = 7 + day
        newday = list(daysoftheweek.values())[day-1]
        newday = ', ' + (list(daysoftheweek.keys())[newday-1]).capitalize()
    else:
        newday = ''

    #  changing the hour value
    newhour = start[0] % 12
    if newhour == 0:
        start[0] = 12
    else:
        start[0] = newhour

    #  putting it all together
    finaltime = str(start[0]) + ':' + start[1] + f' {timeperiod}'
    if dayspassed == 0:
        dayspassed = ''
    elif dayspassed == 1:
        dayspassed= ' (next day)'
    else:
        dayspassed = f' ({dayspassed} days later)'

    new_time = f'{finaltime}{newday}{dayspassed}'.rstrip()
    return new_time

