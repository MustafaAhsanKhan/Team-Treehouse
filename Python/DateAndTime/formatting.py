import datetime

t = datetime.time(hour = 12, minute = 6)
d = datetime.date(2024, 10, 7)
dt = datetime.datetime.combine(d, t)

print(t.strftime("%H:%M"))
print(d.strftime("%a %d/%m/%y"))
print(dt.strftime("%M minutes past %I %p on %B %d"))

# These are some common formats

