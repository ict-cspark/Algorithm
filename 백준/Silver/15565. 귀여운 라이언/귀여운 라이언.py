import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

left = 0
right = 0

value = int(1e9)
cnt = 0
if dolls[0] == 1:
    cnt = 1

while right < N:
    if cnt == K:
        value = min(value, right - left + 1)
        if dolls[left] == 1:
            cnt -= 1
        left += 1
    else:
        right += 1
        if right < N and dolls[right] == 1:
            cnt += 1

if value == int(1e9):
    value = -1

print(value)