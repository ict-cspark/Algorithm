import sys
from collections import deque
input = sys.stdin.readline


def game(K):
    queue = deque([K])

    cnt = 0
    while queue:
        k = queue.popleft()
        if len(tree[k]) == 1 and k != 1:
            cnt += visited[k]
        else:
            for t in tree[k]:
                if visited[t] == -1:
                    visited[t] = visited[k] + 1
                    queue.append(t)

    return cnt


N = int(input())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [-1] * (N + 1)
visited[1] = 0
result = game(1)

if result % 2:
    print('Yes')
else:
    print('No')