# 테스트케이스 입력받기
T = int(input())

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def BFS(sr, sc):
    queue = [(sr, sc)]
    move = [room[sr][sc]]
    if visit[sr][sc] == 0:
        visit[sr][sc] = 1
    else:
        return -1, -1
    while queue:
        r, c = queue.pop(0)
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0 and abs(room[r][c] - room[nr][nc]) == 1:
                queue.append((nr, nc))
                visit[nr][nc] = visit[r][c] + 1
                move.append(room[nr][nc])

    return min(move), len(move)

for test_case in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]

    num = N * N
    count = 0
    for sr in range(N):
        for sc in range(N):
            f, n = BFS(sr, sc)
            if count < n or (count == n and num > f):
                count = n
                num = f

    print(f'#{test_case} {num} {count}')