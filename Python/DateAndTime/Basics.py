import datetime

# time is a class used to handle time
t = datetime.time(20, 30, 5)  # Hour, minute, second

print(t)
print(t.hour)
print(t.second)

# date is a class used to handle date

d = datetime.date(2024, 10, 7)

print(d)
print(d.month)  
print(d.day)

d = datetime.date.today()  # This will automatically assign the current date

print(d)
print(d.month)  
print(d.day)

print(d.weekday())  # Monday is 0
print(d.isoweekday())  # Monday is 1

print(d.isocalendar())  # This is usefull as it gives the week number with respect to the year

# datetime is a class which lets us handle both date and time

dt = datetime.datetime(2024, 7, 10)  # date arguments are required, while the time args are not(default 0)
print(dt.year)
print(dt.second)

dt = datetime.datetime.now()  # this is similar to the .today method for date

print(dt)

dt.date()  # this extracts the "date" part
dt.time()  # this extracts the "time" part