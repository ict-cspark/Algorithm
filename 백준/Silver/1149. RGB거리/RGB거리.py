N = int(input())
color = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        color[i][j] += min(color[i - 1][:j] + color[i - 1][j + 1 :])

print(min(color[-1]))