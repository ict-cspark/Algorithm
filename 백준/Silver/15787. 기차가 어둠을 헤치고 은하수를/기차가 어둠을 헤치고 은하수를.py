import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

trains = dict()
for i in range(1, N + 1):
    trains[i] = deque([0] * 20)

for _ in range(M):
    order = list(map(int, input().split()))

    if order[0] == 1:
        trains[order[1]][order[2] - 1] = 1

    elif order[0] == 2:
        trains[order[1]][order[2] - 1] = 0

    elif order[0] == 3:
        trains[order[1]].appendleft(0)
        trains[order[1]].pop()

    elif order[0] == 4:
        trains[order[1]].append(0)
        trains[order[1]].popleft()

space = []
for j in range(1, N + 1):
    train = list(trains[j])
    if train not in space:
        space.append(train)

result = len(space)
print(result)