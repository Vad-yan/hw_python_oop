import datetime as dt


class Calculator:
    def __init__(self, limit, value=0):
        pass

    def add_record(Record):
        pass

    def get_today_stats():
        pass

    def get_week_stats():
        pass


class CashCalculator(Calculator):
    def get_today_cash_remained(currency):
        pass


class CaloriesCalculator(Calculator):
    def get_calories_remained(currency):
        pass


class Record ():
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date:
            date_format = '%d.%m.%Y'
            moment = dt.datetime.strptime(date, date_format).date()
            self.date = moment
        else:
            self.date = dt.datetime.now().date()

    def getstring(self):
        return f'Потрачено {self.amount} руб. на {self.comment} {self.date}'


r1 = Record(amount=145, comment="Безудержный шопинг")
r2 = Record(amount=568, comment="Наполнение потребительской корзины")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

print(f'Потрачено {r3.amount} руб. на {r3.comment} {r3.date}')
print(r3.getstring())