import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

visited = set()
visited.add(numbers[0])
parent = [0] * (N + 1)
parent[numbers[0]] = -1

for i in range(1, N):
    if numbers[i] not in visited:
        visited.add(numbers[i])
        parent[numbers[i]] = numbers[i - 1]

print(len(visited))
print(*parent[:len(visited)])
