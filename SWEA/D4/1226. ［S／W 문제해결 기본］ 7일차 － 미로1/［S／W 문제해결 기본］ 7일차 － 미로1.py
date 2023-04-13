def MazeStart(arr):
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return i, j
    return -1, -1

def BFS(r, c, arr):
    visit = [[0] * 16 for _ in range(16)]
    delta = [(-1, 0), (0, 1), (1, 0 ), (0, -1)]
    queue = [(r, c)]
    visit[r][c] = 1

    while queue:
        r, c = queue.pop(0)
        if arr[r][c] == 3:
            return 1
        else:
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if 0 < nr < 15 and 0 < nc < 15 and arr[nr][nc] != 1 and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    queue.append((nr, nc))
    return 0


# 테스트케이스 입력받기
T = 10

for _ in range(1, T + 1):
    test_case = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    sR, sC = MazeStart(arr)
    result = BFS(sR, sC, arr)

    print(f'#{test_case} {result}')