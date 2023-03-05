import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]
result = [0] * (T + 1)
result[0] = 1

for p, n in coins:
    for t in range(T, 0, -1):
        for i in range(1, n + 1):
            answer = t - (p * i)
            if answer >= 0:
                result[t] += result[answer]

print(result[T])