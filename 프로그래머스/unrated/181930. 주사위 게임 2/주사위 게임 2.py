def solution(a, b, c):
    if a == b == c:
        mode = 3
    elif a == b or b == c or a == c:
        mode = 2
    else:
        mode = 1
        
    answer = 0
    if mode >= 1:
        answer += (a + b + c)
    if mode >= 2:
        answer *= (a ** 2 + b ** 2 + c ** 2)
    if mode >= 3:
        answer *= (a ** 3 + b ** 3 + c ** 3)
        
    return answer