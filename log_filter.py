import datetime
import re


def date_filter(line):
    if re.search(r"\d{4}\/(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01])", line):
        m = re.search(r"\d{4}\/(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01])", line)
        date_obj = datetime.datetime.strptime(m.group(), "%Y/%m/%d")
        return date_obj.day
    elif re.search(r"(\w{3}\s+\d+\s+[0-9:]+)", line):
        m = re.search(r"(\w{3}\s+\d+\s+[0-9:]+)", line)
        date_obj = datetime.datetime.strptime(m.group(), '%b %d %H:%M:%S')
        return date_obj.day
    elif re.search(r"\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])", line):
        m = re.search(r"\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])", line)
        date_obj = datetime.datetime.strptime(m.group(), "%Y-%m-%d")
        return date_obj.day
    else:
        return
    '''
    elif re.search(r"\d*\.\d*", line):
        m = re.search(r"\d*\.\d*", line)
        ts = int(float(m.group()))
        date_obj = datetime.datetime.fromtimestamp(ts)
        return date_obj.day
    '''
