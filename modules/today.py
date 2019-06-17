from datetime import datetime
def date():
    format = '%m/%d/%Y'
    return datetime.today().strftime(format)
