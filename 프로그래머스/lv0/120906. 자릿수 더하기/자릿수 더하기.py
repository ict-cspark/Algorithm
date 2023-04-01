def solution(n):
    N = str(n)
    
    answer = 0
    for n in N:
        answer += int(n)
    return answer