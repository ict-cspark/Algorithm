import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())

    info = dict()
    score = dict()
    for a in range(n):
        info[a + 1] = [0, 0, 0]
        score[a + 1] = [0] * (k + 1)

    for b in range(m):
        i, j, s = map(int, input().split())
        if score[i][j] < s:
            score[i][j] = s
        info[i][1] += 1
        info[i][2] = b + 1

    for c in range(n):
        info[c + 1][0] = sum(score[c + 1])

    result = sorted(info.items(), key=lambda x: (-x[1][0], x[1][1], x[1][2]))

    for r in range(n):
        if result[r][0] == t:
            print(r + 1)
            break