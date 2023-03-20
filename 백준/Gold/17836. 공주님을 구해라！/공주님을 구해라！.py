import sys
from collections import deque

input = sys.stdin.readline
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
visited = [[0] * M for _ in range(N)]

def BFS():
    gram = 10001
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        r, c = queue.popleft()
        if (r, c) == (N - 1, M - 1):
            return min(visited[r][c] - 1, gram)

        if castle[r][c] == 2:
            gram = visited[r][c] - 1 + (N - 1 - r) + (M - 1 - c)

        for d in range(4):
            nr = r + delta[d][0]
            nc = c + delta[d][1]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if castle[nr][nc] == 0 or castle[nr][nc] == 2:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))

    return gram

result = BFS()
if result > T:
    print("Fail")
else:
    print(result)