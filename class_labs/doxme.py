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
        modules = ''
        if detLang(file) == 'python': modules = applyRegexForPy(lines)
        lines.insert(0, f'#{file};\n#depencancies:{modules if modules else " none;"}\n#last edit: {date.today()}, by {AUTHOR};\n#\n#\n\n')	
        return lines

def write(file, newData):
    with open(file, 'w') as doxedFile:
        for line in newData: doxedFile.write(line)

def detLang(file):
    if re.match('.*\.py', file): return 'python'
    return 'unknown'

def applyRegexForPy(lines):
    mods = ''
    for line in lines:
        if 'import' in line and line[0] != '#':
            mod = re.split("import", line)[1].rstrip()
            if re.search("[]:!?=+()[\-{}]+", mod): pass
            else: mods += f'{mod},'
    return mods[:-1] + ''


def main():
    for file in sys.argv:
        if file == __file__: pass
        else:
            try: write(file, read(file))
            except: print(f'error processing file: {file}')


if __name__ == '__main__': main()


""" to do:
generalize line looping;
add regex for other lang module recognition (node, mjs, php, java, swift)
improve comment recognition (EOL comments, multi-line comments)
improve existing regex (distinguish 'import' && 'from .* import')

"""

