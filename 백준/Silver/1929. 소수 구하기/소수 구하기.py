M, N = map(int, input().split())

if M == 1:
    M = 2

for i in range(M, N + 1):
    answer = int(i ** (1/2)) + 1
    for j in range(2, answer):
        if i % j == 0:
            break
    else:
        print(i)