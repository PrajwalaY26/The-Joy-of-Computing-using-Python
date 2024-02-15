import calendar
days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]

find=input().split()
lis=list(find)
try:
    dayNumber = calendar.weekday(int(lis[2]), int(lis[0]),int(lis[1])) 
    print(days[dayNumber])
except Exception as e:
    
    print(e)