def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        min_num = 1e9
        for i in range(s, e + 1):
            if arr[i] > k and arr[i] < min_num:
                min_num = arr[i]
        if min_num == 1e9:
            answer.append(-1)
        else:
            answer.append(min_num)
    return answer