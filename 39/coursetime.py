from datetime import datetime, timedelta
import os
import re
from typing import List, Tuple, Any
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


def get_all_timestamps() -> list[tuple[int, int]]:
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    result = []
    time_part = re.compile(r'\((\d+:\d+)(:\d+)?\)')
    with open(COURSE_TIMES) as f:
        line = f.readline()
        while line:
            matched = find_match(time_part, line)
            if matched:
                result.append(matched[1])
            line = f.readline()

    return result


def find_match(pattern, line):
    return re.search(pattern, line)


def calc_total_course_duration(timestamps) -> str:
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    durations = []
    for timestamp in timestamps:
        minutes, seconds = timestamp.split(':')
        delta = timedelta(minutes=int(minutes), seconds=int(seconds))
        durations.append(delta)

    total_duration = sum(durations, timedelta())

    # Convert total_duration to hours, minutes, and seconds
    total_hours, remainder = divmod(total_duration.total_seconds(), 3600)
    total_minutes, total_seconds = divmod(remainder, 60)

    return f"{int(total_hours)}:{int(total_minutes)}:{int(total_seconds)}"

