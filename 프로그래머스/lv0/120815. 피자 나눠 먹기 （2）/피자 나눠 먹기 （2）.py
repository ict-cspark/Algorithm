def solution(n):
    for i in range(1, 51):
        temp = i * 6
        if temp % n  == 0:
            answer = i
            break
    return answer