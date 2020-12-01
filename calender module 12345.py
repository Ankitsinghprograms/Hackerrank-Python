import calendar
year=input()
m=int(year.split(" ")[0])
d=int(year.split(" ")[1])
y=int(year.split(" ")[2])

day=calendar.weekday(y,m,d)

if day==0:
	print("MONDAY")
elif day==1:
	print("TUESDAY")
elif day==2:
	print("WEDNESDAY")
elif day==3:
	print("THURSDAY")
elif day==4:
	print("FRIDAY")
elif day==5:
	print("SATURDAY")
elif day==6:
	print("SUNDAY")
