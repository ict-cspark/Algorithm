dr = (1, 1, -1, -1, 1)
dc = (-1, 1, 1, -1, -1)

def DFS(n, fr, fc, v, cnt):
    global r, c, result
    if n == 2 and result >= cnt*2:
        return

    if n > 3:
        return

    if fr == r and fc == c and n == 3 and result < cnt:
        result = cnt
        return

    for k in range(n, n+2):
        nr = fr + dr[k]
        nc = fc + dc[k]
        if 0 <= nr < N and 0 <= nc < N and cafe[nr][nc] not in v:
            v.append(cafe[nr][nc])
            DFS(k, nr, nc, v, cnt + 1)
            v.pop()


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for r in range(N - 2):
        for c in range(1, N - 1):
            DFS(0, r, c, [], 0)

    print(f'#{test_case} {result}')