import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self, today_stats=None):
        amount_sum = 0
        for record in self.records:
            if record.date == dt.datetime.now().date():
                amount_sum += record.amount
        #return f'Потрачено сегодня {amount_sum} руб.'
        return amount_sum
        #for date = today:
        #    ammout=+amount

    def get_week_stats(self):
        amount_sum_week = 0
        for record in self.records:
            if dt.datetime.now().date() >= record.date >= dt.datetime.now().date()-dt.timedelta(days=7):
                amount_sum_week += record.amount
        return amount_sum_week


class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency):
        pass


class CaloriesCalculator(Calculator):
    def get_calories_remained(self, currency):
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

#    def getstring(self):
#        return f'Потрачено {self.amount} руб. на {self.comment} {self.date}'

    def __str__(self):
        return f'Потрачено {self.amount} руб. на {self.comment} {self.date}'



r1 = Record(amount=145, comment="Безудержный шопинг")
r2 = Record(amount=568, comment="Наполнение потребительской корзины")
r3 = Record(amount=691, comment="Катание на такси", date="26.02.2021")

# print(f'Потрачено {r3.amount} руб. на {r3.comment} {r3.date}')
# print(r3.getstring())
print(r3)

cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment="кофе"))
cash_calculator.add_record(r1)
cash_calculator.add_record(r2)
cash_calculator.add_record(r3)
print(cash_calculator.records)

#for elem in cash_calculator.records:
#   print(elem)

print(cash_calculator.get_today_stats())
print(cash_calculator.get_week_stats())


