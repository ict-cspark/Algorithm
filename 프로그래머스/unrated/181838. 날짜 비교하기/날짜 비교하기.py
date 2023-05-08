def solution(date1, date2):
    year1, month1, day1 = date1[0], date1[1], date1[2]
    year2, month2, day2 = date2[0], date2[1], date2[2]
    
    answer = 0
    if year1 <= year2 and month1 <= month2 and day1 < day2:
        answer = 1
    elif year1 <= year2 and month1 < month2:
        answer = 1
    elif year1 < year2:
        answer = 1
    
    return answer