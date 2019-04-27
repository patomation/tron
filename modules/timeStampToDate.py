from datetime import datetime

def convert(timestamp):
    ts = int(timestamp)
    date = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return date
