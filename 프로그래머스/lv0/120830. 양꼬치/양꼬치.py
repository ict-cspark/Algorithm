def solution(n, k):
    k = k - (n // 10)
    if k < 0:
        k = 0
    answer = (n * 12000) + (k * 2000)
    
    return answer