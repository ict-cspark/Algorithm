def solution(balls, share):
    N = 1
    for n in range(balls, 0, -1):
        N *= n
    
    A = 1
    for a in range((balls - share), 0,  -1):
        A *= a
    
    M = 1
    for m in range(share, 0, -1):
        M *= m
        
    B = A * M
    
    answer = N / B
    return answer