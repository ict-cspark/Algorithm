import sys
input = sys.stdin.readline

N, M = map(int, input().split())

guide = dict()

for i in range(1, N + 1):
    pokemon = input().strip()
    guide[pokemon] = i
    guide[str(i)] = pokemon

for _ in range(M):
    search = input().strip()
    print(guide[search]) 