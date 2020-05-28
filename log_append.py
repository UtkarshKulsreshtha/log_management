import datetime
from remove_duplicate_line import remove_duplicate


def line_append(dt_obj, line):
    pdt = datetime.date.today()
    ldt0 = pdt - datetime.timedelta(days=0)
    ldt1 = pdt - datetime.timedelta(days=1)
    ldt2 = pdt - datetime.timedelta(days=2)
    ldt3 = pdt - datetime.timedelta(days=3)
    ldt4 = pdt - datetime.timedelta(days=4)
    ldt5 = pdt - datetime.timedelta(days=5)
    ldt6 = pdt - datetime.timedelta(days=6)
    ldt7 = pdt - datetime.timedelta(days=7)
    ldt8 = pdt - datetime.timedelta(days=8)
    ldt9 = pdt - datetime.timedelta(days=9)
    if dt_obj == ldt0.day:
        with open('/home/gslab/log_files/mylog0.log', 'a+') as f:
            f.write(line)
            f.close()
    elif dt_obj == ldt1.day:
        with open('/home/gslab/log_files/mylog1.log', 'a+') as f:
            f.write(line)
            f.close()
    elif dt_obj == ldt2.day:
        with open('/home/gslab/log_files/mylog2.log', 'a+') as f:
            f.write(line)
            f.close()
    elif dt_obj == ldt3.day:
        with open('/home/gslab/log_files/mylog3.log', 'a+') as f:
            f.write(line)
            f.close()
    elif dt_obj == ldt4.day:
        with open('/home/gslab/log_files/mylog4.log', 'a+') as f:
            f.write(line)
            f.close()
    elif dt_obj == ldt5.day:
        with open('/home/gslab/log_files/mylog5.log', 'a+') as f:
            f.write(line)
            f.close()
    elif dt_obj == ldt6.day:
        with open('/home/gslab/log_files/mylog6.log', 'a+') as f:
            f.write(line)
            f.close()
    elif dt_obj == ldt7.day:
        with open('/home/gslab/log_files/mylog7.log', 'a+') as f:
            f.write(line)
            f.close()
    elif dt_obj == ldt8.day:
        with open('/home/gslab/log_files/mylog8.log', 'a+') as f:
            f.write(line)
            f.close()
    elif dt_obj == ldt9.day:
        with open('/home/gslab/log_files/mylog9.log', 'a+') as f:
            f.write(line)
            f.close()
    else:
        with open('/home/gslab/log_files/mylog_rest.log', 'a+') as f:
            f.write(line)
            f.close()
