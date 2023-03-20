from collections import deque

N, k = map(int, input().split())
lines = [list(map(int, input())) for _ in range(2)]

queue = deque([(0, 0)])
visited = [[0] * N for _ in range(2)]
time = -1
flag = False

while queue:
    for _ in range(len(queue)):
        d, idx = queue.popleft()

        if idx + 1 >= N or idx + k >= N:
            flag = True
            break

        if lines[d][idx + 1] and not visited[d][idx + 1]:
            queue.append((d, idx + 1))
            visited[d][idx + 1] = 1

        if idx - 1 > time + 1 and lines[d][idx - 1] and not visited[d][idx - 1]:
            queue.append((d, idx - 1))
            visited[d][idx - 1] = 1

        if lines[(d + 1) % 2][idx + k] and not visited[(d + 1) % 2][idx + k]:
            queue.append(((d + 1) % 2, idx + k))
            visited[(d + 1) % 2][idx + k] = 1

    time += 1

if flag:
    print(1)
else:
    print(0)