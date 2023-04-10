def clock_number(K):
    answer = int("".join(K))

    for k in range(1, 4):
        temp = int("".join(K[k:] + K[:k]))
        if answer > temp:
            answer = temp

    return answer


N = list(map(str, input().split()))
N = clock_number(N)

result = 1
for i in range(1111, N):
    if '0' not in str(i) and i == clock_number(list(str(i))):
        result += 1

print(result)