import sys
input = sys.stdin.readline

N, M = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

top = N * M

left = 0
for i in range(N):
    left += blocks[i][0]
    for j in range(1, M):
        if blocks[i][j] > blocks[i][j - 1]:
            left += blocks[i][j] - blocks[i][j - 1]

front = 0
for i in range(M):
    front += blocks[0][i]
    for j in range(1, N):
        if blocks[j][i] > blocks[j - 1][i]:
            front += blocks[j][i] - blocks[j - 1][i]

result = (top + left + front) * 2
print(result)