N, M, V = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1


visit = [0] * (N + 1)
visit[V] = 1
stack = []
result = [V]
r = V
while True:             # DFS (스택)
    for c in range(1, N + 1):
        if arr[r][c] == 1 and visit[c] == 0:
            stack.append(r)
            result.append(c)
            visit[c] = 1
            r = c
            break
    else:
        if stack:
            r = stack.pop()
        else:
            break
print(*result)

visit = [0] * (N + 1)
visit[V] = 1
queue = [V]
result = [V]
while queue:            # BFS (큐)
    r = queue.pop(0)
    for c in range(1, N + 1):
        if arr[r][c] == 1 and visit[c] == 0:
            queue.append(c)
            result.append(c)
            visit[c] = 1
print(*result)