import calendar
import math
from datetime import date, timedelta
from typing import Tuple

"""
Sample text if on-track:
Congratulations! You are on track with your steps goal. The target for 2023-01-12 is 164,383 steps and you are 11 ahead.

Sample text if not on track:
You have some catching up to do! The target for 2023-09-30 is 27,300 pages read and you are 2 behind.
"""


def goal_tracker(desc: str, annual_target: int, current_score: int, score_date: Tuple[int, int, int]):
    """Return a string determining whether a goal is on track
     by calculating the current target and comparing it with the current achievement.
     The function assumes the goal is to be achieved in a calendar year. Think New Year's Resolution :)
     """

    # calcuate the beginning date for the goal based on the input year
    start_date = date(score_date[0], 1, 1) - timedelta(days=1)

    # create a date object for date parsed in
    current_date = date(*score_date)

    # fixed end date for when goal ends using year of date entered (assumes goal is set for same year)
    end_date = date(score_date[0], 12, 31)

    # calculate total remaining days
    total_days_remaining = normalize(start_date, end_date)

    # calculate days completed
    days_completed = normalize(start_date, current_date)

    required_amount = calculate_required_amount(annual_target, total_days_remaining, days_completed)

    if math.trunc(required_amount) <= current_score:
        ahead_by = current_score - math.floor(required_amount)
        score = math.trunc(required_amount)
        message = f"Congratulations! You are on track with your {desc} goal. The target for {current_date.isoformat()} is {score:,} {desc} and you are {ahead_by} ahead."
    else:
        behind_by = math.floor(required_amount) - current_score
        behind_score = math.trunc(required_amount)
        message = f"You have some catching up to do! The target for {current_date.isoformat()} is {behind_score:,} {desc} and you are {behind_by} behind."

    return message


"""
Takes in a start and end date and calculates how many days have elapsed"""


def normalize(start_date: date, end_date: date) -> int:
    time_delta = end_date - start_date
    return time_delta.days


"""calculate the total target that is required  to be achieved by the goal date"""


def calculate_required_amount(annual_target: int, total_days: int, days_completed: int) -> float:
    required_amount = (annual_target / total_days) * days_completed
    return required_amount
