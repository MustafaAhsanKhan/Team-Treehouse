from dateutil import relativedelta
import datetime

alarm = datetime.timedelta(hours = 1, minutes = 30)

alarm_time = alarm + datetime.datetime.now()  # Adding 1 hour and 30 minutes to the current time

print(alarm_time)  # This will show what TIME the alarm will go off

# We can even subtract to go back in time

started_work = datetime.datetime(2024, 7, 28, 17)

time_worked = datetime.datetime.now() - started_work

print(time_worked)

alarm = relativedelta.relativedelta(hours = 1, minutes = 30)

alarm_time = alarm + datetime.datetime.now()  # Adding 1 hour and 30 minutes to the current time

print(alarm_time)  # This will show what TIME the alarm will go off