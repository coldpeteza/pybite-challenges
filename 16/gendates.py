from datetime import datetime, timedelta
from itertools import islice
from pprint import pprint

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    current_date = PYBITES_BORN
    interval = timedelta(days=100)
    while True:
        current_date += interval
        yield current_date

#gen = gen_special_pybites_dates()
#pprint(list(islice(gen,2)))