def solution(array, n):
    answer = 0
    for arr in array:
        if arr == n:
            answer += 1
            
    return answer