"""find the number of business days that exist between the date range."""
import pandas as pd

def business_days(d1, d2):
    dates = pd.date_range(d1, d2)
    daynumbers = [i.isoweekday() for i in dates]
    # we need only the days that are Monday through Friday. i.e. 1 through 5
    return len([i for i in daynumbers if i in [1, 2, 3, 4, 5]])


date1 = '2021-01-31'
date2 = '2021-02-18'
print(business_days(date1, date2))
