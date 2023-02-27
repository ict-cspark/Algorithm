import sys
input = sys.stdin.readline

N = int(input())
L = [0] + list(map(int, input().split()))
G = [0] + list(map(int, input().split()))

result = [([0] * 101) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        if L[i] <= j:
            result[i][j] = max(result[i - 1][j], result[i - 1][j - L[i]] + G[i])
        else:
            result[i][j] = result[i - 1][j]

print(result[N][99])