def solution(arr):
    answer = [arr[0]]
    flag = arr[0]
    for i in range(1, len(arr)):
        res = arr[i]
        if flag != res:
            answer.append(res)
            flag = res
    return answer