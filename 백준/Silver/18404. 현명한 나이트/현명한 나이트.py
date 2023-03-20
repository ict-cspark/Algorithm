from collections import deque

delta = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

def BFS(r, c):
    queue = deque()
    queue.append((r, c))
    board[r][c] = 0

    while queue:
        r, c = queue.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == -1:
                queue.append((nr, nc))
                board[nr][nc] = board[r][c] + 1
    return

N, M = map(int, input().split())
board = [[-1] * N for _ in range(N)]
sr, sc = map(int, input().split())
horse = [list(map(int, input().split())) for _ in range(M)]

BFS(sr - 1, sc - 1)
for r, c in horse:
    print(board[r - 1][c - 1], end=' ')