import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

result = 1e9
H = 0
for i in range(257):
    give = 0
    take = 0
    for r in range(N):
        for c in range(M):
            if blocks[r][c] > i:
                give += blocks[r][c] - i
            else:
                take += i - blocks[r][c]

    if take > give + B:
        continue

    cost = take + (give * 2)
    if result >= cost:
        result = cost
        H = i

print(result, H)