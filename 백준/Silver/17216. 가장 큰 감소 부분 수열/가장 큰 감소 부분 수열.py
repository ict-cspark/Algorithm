import sys
input = sys.stdin.readline

A = int(input())
numbers = list(map(int, input().split()))

result = numbers[:]

for i in range(A):
    for j in range(i):
        if numbers[j] > numbers[i]:
            result[i] = max(result[i], result[j] + numbers[i])

print(max(result))