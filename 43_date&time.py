import datetime

date = datetime.date(2025,2,28)
today = datetime.date.today()

print(date)  
print(today)

time = datetime.time(12, 30, 45)
now = datetime.datetime.now()

print(time)
now = now.strftime("time-%H:%M:%S day-%d/%m/%Y")
print(now)


target_datetime = datetime.datetime(2030,2,28, 12, 30, 45)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has already passed.")
else:
    print("Target date is in the future or today.")