def add_time(start, duration, day=""):
    new_time=""
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    #splitting start time
    start_hour = int(start.split(':')[0])
    start_min =int(start.split(':')[1].split()[0])
    period =start.split(':')[1].split()[1]
    if period.upper() =='PM' and start_hour!=12:
        start_hour+=12
    elif period.upper() =='AM' and start_hour ==12:
        start_hour = 0
    print(start_hour, start_min, period)

    #splitting duration time
    duration_hour = int(duration.split(':')[0])
    duration_min =int(duration.split(':')[1])
    print(duration_hour, duration_min)

    new_time_min = start_min + duration_min
    extra_hours = (new_time_min)//60
    final_minute = new_time_min%60
    
    total_hours = extra_hours + start_hour + duration_hour
    days_passed = total_hours//24
    final_hours_24 = total_hours%24

    print(final_hours_24,total_hours,days_passed)
    
    if final_hours_24 == 0:
        display_hour = 12
        period = 'AM'
    elif final_hours_24 <12:
        display_hour = final_hours_24
        period ='AM'
    elif final_hours_24 == 12:
        display_hour = 12
        period = 'PM'
    else:
        display_hour = final_hours_24 - 12
        period = 'PM'

    new_time = f"{display_hour}:{str(final_minute).rjust(2, '0')} {period}"

    # Handle day of the week if provided
    if day:
        day_index = weekdays.index(day.strip().capitalize())
        new_day_index = (day_index + days_passed) % 7
        new_day = weekdays[new_day_index]
        new_time += f", {new_day}"

    # Add day info
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
print(add_time('3:30 PM','2:12'))