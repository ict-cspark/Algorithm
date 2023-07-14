N, K, A, B = map(int, input().split())
pots = [K] * N

day = 0
while pots[0] != 0:
    day += 1
    for i in range(A):
        pots[i] += B

    for j in range(N):
        pots[j] -= 1

    pots.sort()

print(day)