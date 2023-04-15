import sys
input = sys.stdin.readline

N, L = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(N)]
water = sorted(water, key=lambda x: (x[1], x[0]))

result = 0
start = 0
for s, e in water:
    if s < start:
        s = start
    K = e - s

    T = (K // L)
    if K % L > 0:
        T += 1

    start = s + (T * L)
    result += T

print(result)