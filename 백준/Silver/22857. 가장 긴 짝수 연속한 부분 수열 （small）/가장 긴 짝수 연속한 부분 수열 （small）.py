import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

end = 0
even = 0
size = 0
result = 0
for start in range(N):
    while end < N:
        if numbers[end] % 2:
            if even == K:
                break
            else:
                even += 1
        size += 1
        end += 1

    if result < size - even:
        result = size - even

    if numbers[start] % 2:
        even -= 1
    size -= 1

print(result)