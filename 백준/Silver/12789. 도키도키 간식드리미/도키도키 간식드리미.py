import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numbers = deque(map(int, input().split()))
stack = deque()
start = 1
end = N
while start <= end:
    if numbers and numbers[0] == start:
        numbers.popleft()
        start += 1
    elif stack and stack[-1] == start:
        stack.pop()
        start += 1
    else:
        if numbers:
            stack.append(numbers.popleft())
        else:
            if stack[-1] != start:
                break

if start > end:
    print("Nice")
else:
    print("Sad")