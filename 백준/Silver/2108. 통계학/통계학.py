import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

A = round(sum(numbers) / N)

if N % 2:
    C = numbers[N // 2]
else:
    C = numbers[(N // 2) - 1]

cnt = dict()
for num in numbers:
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1

cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
if N > 1 and cnt[0][1] == cnt[1][1]:
    M = cnt[1][0]
else:
    M = cnt[0][0]

R = numbers[-1] - numbers[0]

print(A)
print(C)
print(M)
print(R)