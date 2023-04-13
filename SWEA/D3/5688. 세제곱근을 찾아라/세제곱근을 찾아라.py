# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    result = -1
    K = 1
    while K ** 3 <= N:
        if K ** 3 >= N:
            if K ** 3 == N:
                result = K
            break
        else:
            K += 1

    print(f'#{test_case} {result}')