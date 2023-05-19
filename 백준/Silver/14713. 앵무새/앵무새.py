import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = []
for _ in range(N):
    S = deque(input().split())
    queue.append(S)

L = deque(input().split())
while L:
    word = L.popleft()
    for i in range(N):
        if queue[i] and queue[i][0] == word:
            queue[i].popleft()
            break
    else:
        L.append(word)
        break

answer = "Possible"
if L:
    answer = "Impossible"

for q in queue:
    if q:
        answer = "Impossible"
        break

print(answer)