import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

D = [-1] * (N + 1)
T = [0] * (N + 1)
visited = [0] * (N + 1)

D[R] = 0
T[R] = 1
visited[R] = 1

flag = 1
queue = [R]
while queue:
    r = queue.pop(0)
    for g in graph[r]:
        if visited[g] == 0:
            visited[g] = 1
            D[g] = D[r] + 1
            flag += 1
            T[g] = flag
            queue.append(g)

result = 0
for i in range(1, N + 1):
    result += D[i] * T[i]

print(result)