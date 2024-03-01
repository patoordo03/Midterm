import datetime
a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year
c = a + b
d = "xyz" * (c // 3)
print(a)
print(b)
print(c)
print(d)