def solution(arr):
    for i in range(0, 11):
        num = 2 ** i
        if len(arr) <= num:
            arr = arr + [0] * (num - len(arr))
            break
        
    return arr