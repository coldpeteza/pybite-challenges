from collections import namedtuple
from datetime import datetime

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2 * MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2 * HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2 * DAY, 'yesterday', None),
)


def pretty_date(date: datetime) -> str:
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""

    if not isinstance(date, datetime):
        raise ValueError('Date must be of type datetime')
    elif date > NOW:
        raise ValueError('Date cannot be greater than {}'.format(NOW))
    else:
        result = date.strftime('%m/%d/%y')
        delta_age = NOW - date
        seconds_ago = int(delta_age.total_seconds())

        if seconds_ago < TIME_OFFSETS[0].offset:
            result = TIME_OFFSETS[0].date_str
        elif seconds_ago < TIME_OFFSETS[1].offset:
            result = str.format(TIME_OFFSETS[1].date_str,seconds_ago)
        elif seconds_ago < TIME_OFFSETS[2].offset:
            result = TIME_OFFSETS[2].date_str
        elif seconds_ago < TIME_OFFSETS[3].offset:
            result = str.format(TIME_OFFSETS[3].date_str,seconds_ago // TIME_OFFSETS[3].divider)
        elif seconds_ago < TIME_OFFSETS[4].offset:
            result = TIME_OFFSETS[4].date_str
        elif seconds_ago < TIME_OFFSETS[5].offset:
            result = str.format(TIME_OFFSETS[5].date_str,seconds_ago // TIME_OFFSETS[5].divider)
        elif seconds_ago < TIME_OFFSETS[6].offset:
            result = TIME_OFFSETS[6].date_str

        # if TIME_OFFSETS[6].offset > abs(delta_age.total_seconds()) > TIME_OFFSETS[5].offset:
        #     result = TIME_OFFSETS[6].date_str
        # elif TIME_OFFSETS[4].offset > abs(delta_age.total_seconds()) > TIME_OFFSETS[3].offset:
        #     result = TIME_OFFSETS[4].date_str

    return result
