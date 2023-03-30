import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)
result = [-1] * (N + 1)

visited[R] = 1
result[R] = 0

queue = [R]
while queue:
    r = queue.pop(0)
    for i in graph[r]:
        if visited[i] == 0:
            visited[i] = 1
            result[i] = result[r] + 1
            queue.append(i)

for j in range(1, len(result)):
    print(result[j])