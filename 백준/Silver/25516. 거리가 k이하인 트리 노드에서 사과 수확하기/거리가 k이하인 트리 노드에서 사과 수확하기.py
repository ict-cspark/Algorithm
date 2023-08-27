import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def DFS(n, k):
    global result
    if k > K:
        return

    if visited[n] == 0:
        visited[n] = 1
        if apple[n] == 1:
            result += 1
        for i in tree[n]:
            DFS(i, k + 1)

    return


N, K = map(int, input().split())
tree = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

apple = list(map(int, input().split()))
visited = [0] * N

result = 0
DFS(0, 0)

print(result)