def solution(num, total):
    
    value = total // num
    if num % 2:
        start = value - (num // 2)
    else:
        start = value - (num // 2 - 1)
    
    answer = list(range(start, start + num))
    return answer