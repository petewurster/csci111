#./pw_lab02_makeChange/pw_lab02_makeChange.py;
#depencancies: grinp, LooseChange
#last edit: 2020-05-18, by pWurster;
#
#


from grinp import grinp
from LooseChange import LooseChange

def main():
    x = grinp('Enter a number of cents (less than $1)', 'i', 0, 99)
    change = LooseChange(x)

    print(change.display())

if __name__ == '__main__' : main()
