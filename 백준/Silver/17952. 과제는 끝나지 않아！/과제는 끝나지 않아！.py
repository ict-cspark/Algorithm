import sys
input = sys.stdin.readline

N = int(input())

score = 0
stack = []
for _ in range(N):
    task = list(map(int, input().split()))
    if task[0]:
        stack.append(task)

    if stack:
        stack[-1][2] -= 1

        if stack[-1][2] == 0:
            score += stack[-1][1]
            stack.pop()

print(score)