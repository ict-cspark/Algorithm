import sys
input = sys.stdin.readline

N, M = map(int, input().split())
point = list(map(int, input().split()))
point.sort()

start = 0
end = N - 1

result = 0
while start < end:
    K = point[start] + point[end]
    if K >= M:
        result += 1
        start += 1
        end -= 1
    else:
        start += 1

print(result)