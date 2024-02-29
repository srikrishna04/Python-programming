from datetime import  datetime,timedelta
today= datetime.now()
print('today is:' +str(today))
one_day = timedelta(days=1)
yesterday = today - one_day
print('yesterday was: ' +str(yesterday))
two_week = timedelta(weeks=2)
last_before_week = today - two_week
print('last before week was: ' +str(last_before_week))

from datetime import  datetime
today= datetime.now()
print('day' +str(today.day))
print('month' +str(today.month))
print('year' +str(today.year))
print('hour' +str(today.hour))
print('minute' +str(today.min))
print('second' +str(today.second))
