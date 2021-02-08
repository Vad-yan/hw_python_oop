print("hello vscode")

import datetime as dt
now = dt.datetime.now()
datenow = now.date()
print (datenow)

class Calculator:
    pass

class CashCalculator(Calculator):
    pass

class CaloriesCalculator(Calculator):
    pass

class Record ():
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date:
            self.date = date
        else:
            self.date = datenow
        #self.date = date
    #def show(self):
        #print(f'{self.amount} ({self.comment})  {self.date}')

r1 = Record(amount=145, comment="Безудержный шопинг")
r2 = Record(amount=568, comment="Наполнение потребительской корзины")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

print(f'Потрачено {r3.amount} руб на {r3.comment} {r3.date}')