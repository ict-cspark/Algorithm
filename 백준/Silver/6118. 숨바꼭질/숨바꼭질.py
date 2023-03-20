from collections import deque

def BFS(K):
    queue = deque()
    queue.append(K)
    check[K] = 1

    while queue:
        K = queue.popleft()
        for k in graph[K]:
            if check[k] == 0:
                check[k] = check[K] + 1
                queue.append(k)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0] * (N + 1)
BFS(1)
answer = max(check)
print(check.index(answer), answer -1, check.count(answer))