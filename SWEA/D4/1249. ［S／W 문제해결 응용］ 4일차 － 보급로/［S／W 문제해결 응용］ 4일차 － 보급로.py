delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def BFS(sr, sc):
    queue = [(0, 0)]
    visited[sr][sc] = arr[sr][sc]

    while queue:
        r, c = queue.pop(0)

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] > (visited[r][c] + arr[nr][nc]):
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + arr[nr][nc]

    return visited[N - 1][N - 1]

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[10000] * N for _ in range(N)]
    result = BFS(0, 0)

    print(f'#{test_case} {result}')