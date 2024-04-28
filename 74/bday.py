import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    weekday_of_birthday = calendar.day_name[date.weekday()]
    return weekday_of_birthday