def solution(arr):
    r = len(arr)
    c = len(arr[0])
    if r == c:
        answer = arr
    else:
        n = max(r, c)
        answer = [[0] * n for _ in range(n)]
        for i in range(r):
            for j in range(c):
                answer[i][j] = arr[i][j]

    return answer