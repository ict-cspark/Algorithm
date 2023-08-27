import sys
from collections import deque
input = sys.stdin.readline


def BFS(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1

    while queue:
        t = queue.popleft()

        if visited[b] != 0:
            return visited[b] - 1

        for i in graph[t]:
            if visited[i] == 0:
                visited[i] = visited[t] + 1
                queue.append(i)

    return -1


a, b = map(int, input().split())
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (N + 1)

result =  BFS(a)
print(result)