from datetime import datetime as dt

def time_delta(t1, t2):
    """ absolute seconds between to time stamps """
    fmt = '%a %d %b %Y %H:%M:%S %z'
    t = (dt.strptime(t1, fmt) - dt.strptime(t2, fmt)).total_seconds()
    return str(int(abs(t)))

