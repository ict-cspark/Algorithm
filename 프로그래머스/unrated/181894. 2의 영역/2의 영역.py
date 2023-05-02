def solution(arr):
    start = -1
    end = -1
    for i in range(len(arr)):
        if arr[i] == 2:
            start = i
            break
    
    for j in range(len(arr) - 1, -1, -1):
        if arr[j] == 2:
            end = j
            break
            
    if start == -1 and end == -1:
        answer = [-1]
    else:
        answer = arr[start: end+1]
    return answer