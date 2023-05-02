def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            answer = i
            break
    else:
        answer = -1   
    return answer