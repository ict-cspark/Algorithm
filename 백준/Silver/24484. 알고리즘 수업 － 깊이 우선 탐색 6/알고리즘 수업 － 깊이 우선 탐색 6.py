import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def DFS(r):
    global flag
    idx = sorted(graph[r], reverse=True)
    for i in idx:
        if visited[i] == 0:
            visited[i] = 1
            flag += 1
            T[i] = flag
            D[i] = D[r] + 1
            DFS(i)
            

D = [-1] * (N + 1)
T = [0] * (N + 1)
visited = [0] * (N + 1)

D[R] = 0
T[R] = 1
visited[R] = 1

flag = 1
DFS(R)

result = 0
for j in range(1, N + 1):
    result += D[j] * T[j]

print(result)