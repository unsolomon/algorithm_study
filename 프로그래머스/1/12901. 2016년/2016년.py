import datetime

def solution(a, b):
    days = ['SUN',"MON","TUE","WED","THU","FRI","SAT"]
    date = datetime.date(2016,a,b)
    
    
    
    
    
    return days[(date.weekday() +1)%7]