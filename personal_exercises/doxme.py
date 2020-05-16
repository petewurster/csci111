#doxme.py;
#depencancies: sys, re, date;
#last edit: 2020-05-13, by pWurster;
#desc: adds documentation to files as per prof Herbert's spec
#pass any number of files to update in bulk

import sys
import re
from datetime import date

AUTHOR = 'pWurster'

def read(file):
    with open(file, 'r') as original:
        lines = original.readlines()
        mods = ''
        for line in lines:
#### add a func to determine language
            if 'import' in line and line[0] != '#':
                mod = re.split("import", line)[1].rstrip()
#### regex needs streamlining
                if re.search("[]:!?=+()[\-{}]+", mod): pass
                else: mods += f'{mod},'
            mods = mods[:-1] + ''
        lines.insert(0, f'#{file};\n#depencancies:{mods if mods else " none;"}\n#last edit: {date.today()}, by {AUTHOR};\n#desc:\n')	
        return lines

def write(file, data):
    with open(file, 'w') as documented:
        for line in data: documented.write(line)

def main():
    for file in sys.argv:
        if file == __file__: pass
        else:
            try: write(file, read(file))
            except: print(f'error processing file: {file}')

if __name__ == '__main__': main()
