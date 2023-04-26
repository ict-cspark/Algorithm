import sys
input = sys.stdin.readline

N, M = map(int, input().split())

guide = [""] + [input().strip() for _ in range(N)]

for _ in range(M):
    search = input().strip()
    if search.isdecimal():
        print(guide[int(search)])
    else:
        print(guide.index(search))