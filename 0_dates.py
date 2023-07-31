import datetime

gvr = datetime.date(1989,9,13)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)
mill = datetime.date(200,1,1)
dt = datetime.timedelta(100)
print(mill + dt)
print(gvr.strftime("%A,%B,%d,%Y"))
message = "GVR was born on {:%A,%B %d,%Y}."
print(message.format(gvr))
launch_time = datetime.time(22,27,0)
print(launch_time)
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)
now = datetime.datetime.today()
print(now)
print(now.microsecond)

