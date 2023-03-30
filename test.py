import datetime


now_date = datetime.date.today()  # Текущая дата
delta = datetime.timedelta(days=10)  # Для разницы между двумя датами

delta_date = now_date + delta  # Текущая дата + 10 дней
str(now_date.strftime("%d/%m/%Y"))