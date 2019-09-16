import datetime as d

today=d.datetime.today()

year=d.datetime.today().year
month=d.datetime.today().month
day=d.datetime.today().day
hour=d.datetime.today().hour
minute=d.datetime.today().minute
second=d.datetime.today().second

print('Today:{}'.format(today))
print('{}y {}m {}d'.format(year,month,day),end=' ')
print('{}hr {}min {}sec'.format(hour,minute,second))

d1=today.strftime('%Y-%m-%d,%H:%M:%S')
print(d1)

d1=d.datetime.strptime('2017-12-21 14:00:38','%Y-%m-%d %H:%M:%S')

print('current time:',end=' ')
print(d1)

print('\nchange time\n')
d2=d1.replace(year=2000, month=5, day=15)

print('changed time:', end=' ')
print(d2)

ts=today.timetuple()
print('timestamp: ',ts)
print('current time is {}y {}m {}d {}hr {}min {}sec'.format(
ts.tm_year,ts.tm_mon,ts.tm_mday,ts.tm_hour,ts.tm_min,ts.tm_sec))

date1=d.date(2016,12,24)
date2=d.date(year,month,day)
date3=date2-date1
print('first day:{}'.format(date1))
print('today:{}'.format(date2))
print('{}th day'.format(date3))
