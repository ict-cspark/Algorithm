import sys
input = sys.stdin.readline


def DFS(r, c, apple, cnt):
    global result

    if cnt <= 3 and apple >= 2:
        result = 1
        return
    if cnt > 3:
        return

    visited[r][c] = 1
    for dr, dc in delta:
        nr = dr + r
        nc = dc + c
        if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc] != 1:
            if board[nr][nc] == 1:
                DFS(nr, nc, apple + 1, cnt + 1)
            elif board[nr][nc] == 0:
                DFS(nr, nc, apple, cnt + 1)
    visited[r][c] = 0

    return


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
board = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
r, c = map(int, input().split())

result = 0
DFS(r, c, 0, 0)
print(result)