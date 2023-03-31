import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def DFS(r):
    global flag
    G = sorted(graph[r], reverse=True)
    for g in G:
        if visited[g] == 0:
            visited[g] = 1
            flag += 1
            T[g] = flag
            D[g] = D[r] + 1
            DFS(g)


N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)
T = [0] * (N + 1)
D = [-1] * (N + 1)

flag = 1
visited[R] = 1
T[R] = flag
D[R] = 0
DFS(R)

result = 0
for i in range(1, N + 1):
    result += T[i] * D[i]

print(result)