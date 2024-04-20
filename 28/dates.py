import collections
from datetime import datetime
import os
import re
from typing import List
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
RSS_FEED = 'pybites_feed.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = os.getenv("TMP", "/tmp")


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


def convert_to_datetime(date_str: str) -> datetime:
    """Receives a date str and convert it into a datetime object"""
    expected_date_format = "%a, %d %b %Y %H:%M:%S %z"
    return datetime.strptime(date_str, expected_date_format)


def get_month_most_posts(dates: List[datetime]) -> str:
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    counts = dict()
    for date in dates:
        date_part = date.strftime('%Y-%m')
        if counts.get(date_part):
            counts[date_part] += 1
        else:
            counts[date_part] = 1

    max_count = 0
    key = 0
    for date, count in counts.items():
        if count > max_count:
            max_count = count
            key = date

    return key
