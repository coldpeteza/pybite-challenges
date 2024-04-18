from datetime import timedelta, date


def tomorrow(today=None):
    # Your code goes here
    if today is None:
        today = date.today()#.replace(hour=0, minute=0, second=0, microsecond=0)

    next_day = today + timedelta(days=1)

    return next_day
