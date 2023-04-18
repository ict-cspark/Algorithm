import sys
input = sys.stdin.readline

K, N = map(int, input().split())
numbers = [int(input()) for _ in range(K)]

start = 1
end = max(numbers)

while start <= end:
    mid = (start + end) // 2
    answer = 0
    for num in numbers:
        answer += num // mid

    if answer >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)