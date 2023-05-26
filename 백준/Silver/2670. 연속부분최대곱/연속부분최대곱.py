import sys
input = sys.stdin.readline

N = int(input())

DP = [float(input().strip()) for _ in range(N)]

for i in range(1, N):
    DP[i] = max(DP[i], DP[i] * DP[i - 1])

print('%0.3f' % max(DP))