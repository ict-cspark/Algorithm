T = 10

for test_case in range(1, T + 1):
    N, pwd = map(str, input().split())
    result = [pwd[0]]
    password = pwd[1:]
    for p in password:
        if len(result) != 0 and p == result[-1]:
            result.pop(-1)
        else:
            result.append(p)

    print(f'#{test_case} {"".join(result)}')