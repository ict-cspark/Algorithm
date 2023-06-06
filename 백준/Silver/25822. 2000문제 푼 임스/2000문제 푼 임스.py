import sys
input = sys.stdin.readline

C = float(input())
C = int(min(2, C // (0.99)))

N = int(input())
problems = list(map(int, input().split()))

streak = [0] * (N + 1)
p_max = problems[0]
for i in range(N):
    if problems[i] == 0:
        streak[i + 1] = streak[i] + 1
    else:
        streak[i + 1] = streak[i]
    p_max = max(p_max, problems[i])

left = 1
right = 1
d_max = 0
while right <= N:
    buy = streak[right] - streak[left - 1]
    if buy <= C:
        d_max = max(d_max, right - left + 1)
        right += 1
    else:
        left += 1

print(d_max)
print(p_max)