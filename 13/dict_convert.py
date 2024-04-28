from collections import namedtuple
from datetime import datetime
import json

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
Blog = namedtuple('Blog', 'name founders started tags location site')


def dict2nt(dict_):
    result = Blog(name=dict_['name'], founders=dict_['founders'], started=dict_['started'],
                  tags=dict_['tags'], location=dict_['location'], site=dict_['site'])
    return result


def nt2json(nt):
    result = nt._asdict()

    for key, value in result.items():
        if type(value) is datetime:
            result[key] = value.isoformat()

    return json.dumps(result, indent=2)
