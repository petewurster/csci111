#LooseChange.py;
#depencancies: none;
#last edit: 2020-05-18, by pWurster;
#
#

class LooseChange():
    def __init__(self, r):
        self.quarters = r // 25
        self.dimes = r % 25 // 10
        self.nickels = r % 25 % 10 // 5
        self.pennies = r % 25 % 10 % 5
        self._total = self.getTotal()


    def display(self):
        toStr = f'{self._total} cents converts to:\n'
        for key in self.__dict__.keys():
            if not key.startswith('_'):
                toStr += f'\t{self.__dict__[key]} {key}\n'
        return(toStr)


    def getTotal(self):
        return(self.quarters * 25 + self.dimes * 10 + self.nickels * 5 + self.pennies)


