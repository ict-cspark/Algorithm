N = int(input())

DP = [1, 1]
for i in range(2, N + 1):
    answer = 0
    for j in range(i):
        answer += DP[j] * DP[(i - 1) - j]
    DP.append(answer)

print(DP[N])