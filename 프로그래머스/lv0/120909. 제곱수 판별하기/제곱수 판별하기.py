def solution(n):
    answer = 0
    result = n ** (1/2)
    if result % 1 == 0:
        answer = 1
    else:
        answer = 2
    return answer