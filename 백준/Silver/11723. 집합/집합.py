import sys
input = sys.stdin.readline

M = int(input())

S = [0] * 21
for _ in range(M):
    order = list(input().split())
    if len(order) > 1:
        order[1] = int(order[1])

    if order[0] == 'check':
        if S[order[1]]:
            print(1)
        else:
            print(0)
    elif order[0] == 'add':
        S[order[1]] = 1
    elif order[0] == 'remove':
        if S[order[1]]:
            S[order[1]] = 0
    elif order[0] == 'toggle':
        S[order[1]] = (S[order[1]] + 1) % 2
    elif order[0] == 'all':
        S = [1] * 21
    elif order[0] == 'empty':
        S = [0] * 21