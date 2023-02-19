import sys, itertools
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

distance = [0] * (N - 1)
for i in range(1, N):
    distance[i - 1] = sensors[i] - sensors[i - 1]

distance.sort()
result = 0
for j in range(N - K):
    result += distance[j]

print(result)