import pytz

MIN_MEETING_HOUR = 6
MAX_MEETING_HOUR = 22
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """
    Receive a utc datetime and one or more timezones and check if
    they are all within MIN_MEETING_HOUR and MAX_MEETING_HOUR
    (both included).
    """
    begin_time = pytz.utc.fromutc(utc)
    tz_count = len(timezones)
    for tz in timezones:
        if tz not in TIMEZONES:
            raise ValueError('Invalid timezone')
        localtime = begin_time.astimezone(pytz.timezone(tz))
        if MIN_MEETING_HOUR <= localtime.hour <= MAX_MEETING_HOUR:
            tz_count -= 1

    return tz_count == 0
