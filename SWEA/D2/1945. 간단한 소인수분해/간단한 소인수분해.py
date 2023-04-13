T = int(input())

for test_case in range(1, T + 1):

    num = int(input())
    prime = [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]

    for p in range(5):
        while num%prime[p] == 0:
            num = num/prime[p]
            result[p] += 1

    result = " ".join(map(str, result))
    print(f'#{test_case} {result}')