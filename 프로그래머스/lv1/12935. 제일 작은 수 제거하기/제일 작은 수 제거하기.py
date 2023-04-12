def solution(arr):
    answer = []
    a = min(arr)
    arr.remove(a)
    answer = arr
    
    if answer == []:
        answer = [-1]
    return answer