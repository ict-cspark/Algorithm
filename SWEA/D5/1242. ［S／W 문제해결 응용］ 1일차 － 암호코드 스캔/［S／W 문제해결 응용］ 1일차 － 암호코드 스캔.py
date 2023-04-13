code = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    ARR = [input().rstrip() for _ in range(N)]
    ARR = list(set(ARR))
    ARR.remove('0' * M)

    password = []
    for hexa in ARR:
        bina = ''
        for h in hexa:
            deci = int(h, base=16)
            bina += format(deci, 'b').zfill(4)
        password.append(bina)

    result = []
    for pwd in password:
        start = (M * 4) - 1
        while start >= 55:
            numbers = ['-'] * 8
            if pwd[start] == '1':
                for i in range(7, -1, -1):
                    pt1 = 0
                    while pwd[start] == '1':
                        pt1 += 1
                        start -= 1
                    pt2 = 0
                    while pwd[start] == '0':
                        pt2 += 1
                        start -= 1
                    pt3 = 0
                    while pwd[start] == '1':
                        pt3 += 1
                        start -= 1
                    while pwd[start] == '0':
                        start -= 1

                    K = min(pt1, pt2, pt3)
                    key = str(pt3//K) + str(pt2//K) + str(pt1//K)
                    numbers[i] = code[key]

                value = 0
                for v in range(0, 8, 2):
                    value += numbers[v] * 3
                    value += numbers[v + 1]

                if value % 10 == 0:
                    result.append(tuple(numbers))
            else:
                start -= 1

    result = list(set(result))
    answer = 0
    for ans in result:
        answer += sum(ans)
    print(f'#{test_case} {answer}')