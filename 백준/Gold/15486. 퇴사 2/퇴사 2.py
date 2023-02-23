import sys
input = sys.stdin.readline

N = int(input())
day = [0]
cost = [0]

for _ in range(N):
    d, c = map(int, input().split())
    day.append(d)
    cost.append(c)

profit = [0] * (N + 1)

for i in range(1, N + 1):
    profit[i] = max(profit[i - 1], profit[i])
    now = i + day[i] - 1
    if now <= N:
        profit[now] = max(profit[now], profit[i - 1] + cost[i])

print(max(profit))