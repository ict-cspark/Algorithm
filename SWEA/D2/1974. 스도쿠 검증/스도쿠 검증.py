def check(ARR):
    for r in range(9):
        cnt = [0] * 10
        for c in range(9):
            t = ARR[r][c]
            if cnt[t] == 1:
                return 0
            else:
                cnt[t] = 1
    return 1

def check3(ARR):
    for stR in range(0, 9, 3):
        for stC in range(0, 9, 3):
            cnt = [0] * 10
            for r in range(3):
                for c in range(3):
                    t = ARR[stR+r][stC+c]
                    if cnt[t] == 1:
                        return 0
                    else:
                        cnt[t] = 1
    return 1

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    ARR = [list(map(int, input().split())) for _ in range(9)]
    ARR_C = list(map(list, zip(*ARR)))


    result1 = check(ARR)
    result2 = check(ARR_C)
    result3 = check3(ARR)

    if result1 == 0 or result2 == 0 or result3 == 0:
        result = 0
    else:
        result = 1

    print(f'#{test_case} {result}')