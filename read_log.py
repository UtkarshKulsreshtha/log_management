import os
from pathlib import Path

import remove_duplicate_line
import append_log
from list_of_files import getListOfFiles

import log_filter

if __name__ == '__main__':
    p = Path('/var/log')
    list_of_files = getListOfFiles(p)
    n = input("Enter number of days:")

    for file_name in list_of_files:
        if file_name.endswith('.log'):
            FI = open(file_name, 'r')

            for line in FI:
                d_obj = log_filter.date_filter(line)
                append_log.append_line(d_obj, line, n)
            FI.close()
    p1 = Path('/home/gslab/log_files')
    p2 = Path('/home/gslab/test')
    for file in os.listdir(p1):
        remove_duplicate_line.remove_duplicate(p1.joinpath(file), p2.joinpath(file))
