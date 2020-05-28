import datetime
from pathlib import Path


def append_line(dt_obj, line, n):
    pdt = datetime.date.today()
    lst = []
    path = Path('/home/gslab/log_files')
    for i in range(0, int(n)):
        lst.insert(i, pdt - datetime.timedelta(days=i))

    for j in range(0, int(n)):
        if dt_obj == lst[j].day:
            with open(path.joinpath(str(j)), 'a+') as f:
                f.write(line)
                f.close()
