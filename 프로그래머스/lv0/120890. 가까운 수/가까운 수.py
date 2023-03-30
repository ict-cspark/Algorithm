def solution(array, n):
    gap = 999
    result = 0
    
    for a in array:
        if abs(a - n) < gap:
            gap = abs(a - n)
            result = a
        elif abs(a - n) == gap and a < result:
            result = a
    
    answer = result
    return answer