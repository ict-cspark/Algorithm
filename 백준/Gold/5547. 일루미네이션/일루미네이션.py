from collections import deque
import sys

input = sys.stdin.readline
dr = [0, 1, 1, 0, -1, -1]
dc = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]]

W, H = map(int, input().split())
wall = [0] * (W + 2)
graph = [wall] + [[0] + list(map(int, input().split())) + [0] for _ in range(H)] + [wall]

def BFS(r, c):
    queue = deque()
    queue.append((r, c))
    visited = [[0] * (W + 2) for _ in range(H + 2)]
    visited[r][c] = 1
    answer = 0

    while queue:
        r, c = queue.popleft()
        for d in range(6):
            nr = r + dr[d]
            nc = c + dc[r % 2][d]
            if 0 <= nr < H + 2 and 0 <= nc < W + 2:
                if graph[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
                elif graph[nr][nc] == 1:
                    answer += 1

    return answer

result = BFS(0, 0)
print(result)