from collections import deque
import sys
input = sys.stdin.readline


K = int(input())

numbers = deque()
for _ in range(K):
    number = int(input())
    if number:
        numbers.append(number)
    else:
        numbers.pop()

result = sum(numbers)
print(result)