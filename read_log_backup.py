import glob
import os
from pathlib import Path

import log_append
import log_filter
from remove_duplicate_line import remove_duplicate

if __name__ == '__main__':
    p = Path('/var/log/audit')
    list_of_files = p.glob('./*.log')  # create the list of file

    for file_name in list_of_files:
        FI = open(file_name, 'r')

        for line in FI:
            d_obj = log_filter.date_filter(line)
            log_append.line_append(d_obj, line)
        FI.close()
