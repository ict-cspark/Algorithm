def solution(n):
    answer = 0
    flag = 0
    while flag < n:
        answer += 1
        if answer % 3 != 0 and '3' not in str(answer):
            flag += 1
        
    return answer