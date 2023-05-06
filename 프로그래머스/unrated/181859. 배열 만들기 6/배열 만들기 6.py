def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if answer:
            if answer[-1] == arr[i]:
                answer.pop()
            else:
                answer.append(arr[i])
        else:
            answer.append(arr[i])
            
        i += 1
    
    if not answer:
        answer = [-1]
    return answer