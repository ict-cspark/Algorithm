import sys
input = sys.stdin.readline

N = int(input())
boards = [list(map(int, input().split())) for _ in range(N)]
maps = [[0] * N for _ in range(N)]

maps[0][0] = 1
for r in range(N):
    for c in range(N):
        if boards[r][c] == 0:
            break

        if maps[r][c] != 0:
            delta = boards[r][c]
            nr = r + delta
            nc = c + delta
            if 0 <= nr < N:
                maps[nr][c] += maps[r][c]
            if 0 <= nc < N:
                maps[r][nc] += maps[r][c]

print(maps[N - 1][N - 1])