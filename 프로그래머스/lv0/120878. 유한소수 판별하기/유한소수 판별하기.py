def solution(a, b):
    N = min(a, b)
    for i in range(N, 0, -1):
        if a % i == 0 and b % i == 0:
            T = i
            break
            
    a = a // T
    b = b // T
    
    answer = 1
    while b > 1:
        if b % 2 == 0:
            b = b // 2
        elif b % 5 == 0:
            b = b // 5
        else:
            answer = 2
            break
            
    return answer