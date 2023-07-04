import sys
input = sys.stdin.readline

N, M = map(int, input().split())
images = [list(input().strip()) for _ in range(N)]

w = 1001
for i in range(N):
    c = images[i][0]
    r = 1
    for j in range(1, M):
        if c == images[i][j]:
            r += 1
        else:
            w = min(w, r)
            c = images[i][j]
            r = 1

if w == 1001:
    w = M

if M % w != 0:
    w = 1

h = 1001
for i in range(M):
    c = images[0][i]
    r = 1
    for j in range(1, N):
        if c == images[j][i]:
            r += 1
        else:
            h = min(h, r)
            c = images[j][i]
            r = 1

if h == 1001:
    h = N

if N % h != 0:
    h = 1

print(N//h, M//w)
for i in range(0, N, h):
    for j in range(0, M, w):
        print(images[i][j], end="")
    print()