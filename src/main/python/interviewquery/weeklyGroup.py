"""
Given a list of timestamps in sequential order, return a list of lists grouped by week (7 days) using the first timestamp as the starting point.
"""

from collections import defaultdict
from datetime import datetime

def read_date(date):
    return datetime.strptime(date, "%Y-%m-%d")

def weeks_from_date(starting_date, date):
    delta = read_date(date) - read_date(starting_date)
    return delta.days

def weekly_aggregation(ts):
    starting_date = ts[0]
    weekly = defaultdict(list)
    for date in ts:
        weekly[weeks_from_date(starting_date, date) % 7].append(date)
    return list(weekly.values())


ts = [
    '2019-01-01',
    '2019-01-02',
    '2019-01-08',
    '2019-02-01',
    '2019-02-02',
    '2019-02-05',
]
print(weekly_aggregation(ts))
