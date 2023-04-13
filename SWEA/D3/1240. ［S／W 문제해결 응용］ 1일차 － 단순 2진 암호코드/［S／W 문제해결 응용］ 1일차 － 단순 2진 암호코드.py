passcode = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    password = [input() for _ in range(N)]

    result = 0
    for i in range(N):
        pw = password[i]

        start = 0
        for j in range(M - 1, -1, -1):
            if pw[j] == '1':
                start = j + 1
                break

        code = []
        value = 0
        if start > 55:
            answer = pw[start - 56 : start]
            for k in range(0, 56, 7):
                ans = answer[k : k+7]
                code.append(passcode.index(ans))
            for l in range(0, 8, 2):
                value += (code[l] * 3)
                value += code[l + 1]
            if value%10 == 0:
                result = sum(code)
            else:
                result = 0

    print(f'#{test_case} {result}')