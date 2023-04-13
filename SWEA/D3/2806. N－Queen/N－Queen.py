def check(sr, sc):
    for i in range(sr - 1, -1, -1):
        if visited[i][sc] == 1:
            return 0

    li = sr - 1
    lj = sc - 1
    while li >= 0 and lj >= 0:
        if visited[li][lj] == 1:
            return 0
        li -= 1
        lj -= 1

    ri = sr - 1
    rj = sc + 1
    while ri >= 0 and rj < N:
        if visited[ri][rj] == 1:
            return 0
        ri -= 1
        rj += 1

    return 1

def DFS(r):
    global result
    if r == N:
        result += 1
        return
    else:
        for c in range(N):
            if check(r, c):
                visited[r][c] = 1
                DFS(r + 1)
                visited[r][c] = 0
    return


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]

    result = 0
    DFS(0)
    print(f'#{test_case} {result}')