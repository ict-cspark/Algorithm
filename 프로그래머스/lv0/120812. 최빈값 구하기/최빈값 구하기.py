def solution(array):
    number = [0] * 1001
    for a in array:
        number[a] += 1
    
    ans = max(number)
    cnt = number.count(ans)
    if cnt == 1: 
        answer = number.index(ans)   
    else:
        answer = -1
    
    return answer