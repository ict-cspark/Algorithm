import sys
input = sys.stdin.readline

C, N = map(int, input().split())
hotels = [list(map(int, input().split())) for _ in range(N)]

price = [0] + [float('INF')] * (C + 100)

for cost, person in hotels:
    for i in range(person, len(price)):
        price[i] = min(price[i - person] + cost, price[i])

print(min(price[C:]))