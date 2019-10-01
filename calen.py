import calendar
def findday(date):
    day,month,year=(int(i) for i in date.split())
    daynum=calendar.weekday(year,month,day)
    days=["monday","tuesday","wednesday","thursday","friday","saturday","  sunday"]
    return(days[daynum])
date='27 09 2019'
print(findday(date))
