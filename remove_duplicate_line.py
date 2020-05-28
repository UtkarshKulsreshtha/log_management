from pathlib import Path
from tempfile import TemporaryFile


def remove_duplicate(filename, new_filename):
    line_seen = set()
    with open(new_filename, 'w') as fp:
        for line in open(filename, 'r'):
            if line not in line_seen:
                fp.write(line)
                line_seen.add(line)
    fp.close()
