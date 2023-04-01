def solution(num, k):
    num = str(num)
    k = str(k)
    answer = num.find(k)
    
    if answer != -1:
        answer += 1
    return answer