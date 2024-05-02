from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    dt = utc.fromutc(naive_utc_dt)

    spain_dt = dt.astimezone(SPAIN)
    aust_dt = dt.astimezone(AUSTRALIA)

    return aust_dt, spain_dt
