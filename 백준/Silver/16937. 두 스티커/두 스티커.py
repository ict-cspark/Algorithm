import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())
stickers = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(i + 1, N):
        ar, ac = stickers[i]
        br, bc = stickers[j]

        if (ar + br <= H and max(ac, bc) <= W) or max(ar, br) <= H and ac + bc <= W:
            result = max(result, ar * ac + br * bc)
        if (ar + bc <= H and max(ac, br) <= W) or max(ar, bc) <= H and ac + br <= W:
            result = max(result, ar * ac + br * bc)
        if (ac + br <= H and max(ar, bc) <= W) or max(ac, br) <= H and ar + bc <= W:
            result = max(result, ar * ac + br * bc)
        if (ac + bc <= H and max(ar, br) <= W) or max(ac, bc) <= H and ar + br <= W:
            result = max(result, ar * ac + br * bc)

print(result)