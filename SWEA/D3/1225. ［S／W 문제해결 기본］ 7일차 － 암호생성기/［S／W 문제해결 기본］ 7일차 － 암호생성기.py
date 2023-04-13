def password(pwd):
    idx = -1
    while True:
        for i in range(5):
            idx += 1
            ni = idx%8
            pwd[ni] -= (i + 1)
            if pwd[ni] <= 0:
                pwd[ni] = 0

                result = pwd[ni + 1 :] + pwd[: ni + 1]
                result = ' '.join(map(str, result))
                return result

# 테스트케이스 입력받기
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    pwd = list(map(int, input().split()))

    result = password(pwd)

    print(f'#{test_case} {result}')