T = 10

for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for r in range(N):
        isRed = False
        for c in range(N):
            if table[c][r] == 1:
                isRed = True
            elif table[c][r] == 2 and isRed == True:
                result += 1
                isRed = False

    print(f'#{test_case} {result}')