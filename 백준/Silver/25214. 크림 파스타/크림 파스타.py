import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

DP = [0] * N
min_num = A[0]
for i in range(1, N):
    min_num = min(min_num, A[i])
    DP[i] = max(DP[i - 1], A[i] - min_num)

print(*DP)