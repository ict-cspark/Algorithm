import sys
input = sys.stdin.readline

N, M = map(int, input().split())

G = dict()
P = dict()

for _ in range(N):
    group = input().strip()
    n = int(input())

    member = []
    for _ in range(n):
        m = input().strip()
        member.append(m)
        P[m] = group

    member.sort()
    G[group] = member

for _ in range(M):
    keyword = input().strip()
    sort = int(input())
    if sort:
        print(P[keyword])
    else:
        data = G[keyword]
        for name in data:
            print(name)