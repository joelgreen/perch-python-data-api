import datetime


def unix_time_seconds(utc_datetime):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (utc_datetime - epoch).total_seconds()
