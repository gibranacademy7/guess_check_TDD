
# file: days_of_week.py

# def get_day_of_week(number):
#    pass

# file: days_of_week.py

def get_day_of_week(number):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    if number not in days:
        raise ValueError("Number must be between 1 and 7")
    return days[number]
