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