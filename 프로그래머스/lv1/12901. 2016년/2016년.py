import calendar
def solution(a,b):
    day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer = day[calendar.weekday(2016,a,b)]
    return answer