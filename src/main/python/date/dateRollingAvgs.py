"""Given a list of (date, duration) tuples,
how would you filter by time period and calculate summary stats (average, rolling sum) """
from datetime import datetime, timedelta

def get_window_dates(date):
    # Monday is 0, Sunday = 6
    window_beg_date = date - timedelta(days=date.weekday())
    # set to midnight
    window_beg_date.replace(minute=0, hour=0, second=0, microsecond=0)
    window_end_date = window_beg_date + timedelta(7)
    return window_beg_date, window_end_date

def read_date(date):
    return datetime.strptime(date, "%Y-%m-%d")

def rolling_sum(arr):
    window = []
    moving_avgs = []
    cum_sum = []
    for i, t in enumerate(arr):
        date = read_date(t[0])
        value = t[1]
        if i == 0:
            window_beg_date, window_end_date = get_window_dates(date)
        # array is sorted by date. trigger moving avg calculation and reset
        if date >= window_end_date:
            moving_avgs.append(round(sum(window) / len(window), 2))
            prev_sum = cum_sum[-1] if len(cum_sum) > 0 else 0
            # cumulative sum is continuous adding to previous sum
            cum_sum.append(prev_sum + sum(window))
            window = []
            window_beg_date = window_end_date
            window_end_date = window_beg_date + timedelta(7)

        window.append(value)
    # need to calculate one last time
    moving_avgs.append(round(sum(window) / len(window), 2))
    cum_sum.append(cum_sum[-1] + sum(window))
    return moving_avgs, cum_sum


arr = [('2022-01-01', 10),
       ('2022-01-03', 5), ('2022-01-07', 20), ('2022-01-08', 32),
       ('2022-01-11', 25), ('2022-01-14', 12),
       ('2022-01-17', 13), ('2022-01-19', 14)]
moving_averages, cum_sum = rolling_sum(arr)
print("Moving Avg is: ")
print(*moving_averages, sep=", ")
print("Cumulative Sum is: ")
print(*cum_sum, sep=", ")
