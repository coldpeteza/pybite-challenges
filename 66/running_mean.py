import operator
from itertools import accumulate, count, starmap
from functools import reduce
import numpy as np


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    result = []
    total = 0
    for index, item in enumerate(sequence, start=1):
        partial = sequence[:index]
        total = sum(partial)
        if index == 1:
            result.append(total)
            continue

        number_of_records = len(result) + 1
        result.append(round(total/number_of_records,2))

    return result


def meanable(acc, next, bucket):
    print(acc, next, bucket)
    return acc + next
