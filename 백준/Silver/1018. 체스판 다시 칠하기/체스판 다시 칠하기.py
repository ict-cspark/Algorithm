N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]

WC = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
BC = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']


def check(sr, sc, flag):
    global count

    answer = 0
    for r in range(sr, 8 + sr):
        row = board[r][sc:8 + sc]
        if flag:
            compare = BC
        else:
            compare = WC
        for c in range(8):
            if row[c] != compare[c]:
                answer += 1

        flag = not(flag)

    if count > answer:
        count = answer
    return


count = 999
for i in range(N - 7):
    for j in range(M - 7):
        check(i, j, False)
        check(i, j, True)

print(count)