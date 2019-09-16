import calendar as cal

c=cal.calendar(2018)

print("2018's calendar")
print(c)

print("calendar")

year=int(input("born year in:"))
month=int(input("born month in:"))
print(cal.month(year,month)) 

print("day check-in")
year=int(input("year:"))
month=int(input("month:"))
day=int(input("day:"))
week=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
q=cal.weekday(year,month,day)

print(week[q],"day")