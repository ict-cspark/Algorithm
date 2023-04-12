def solution(n):
    for i in range(1,n+1):
        if n/i == i:
            return pow(i+1,2)
    return -1