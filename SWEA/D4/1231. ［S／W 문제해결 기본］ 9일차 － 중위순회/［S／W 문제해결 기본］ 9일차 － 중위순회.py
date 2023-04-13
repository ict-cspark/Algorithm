def in_order(v):
    if v:
        global result
        in_order(ch1[v])
        result += V_info[v]
        in_order(ch2[v])

# 테스트케이스 입력받기
T = 10

for test_case in range(1, T + 1):
    V = int(input())
    info = [list(map(str, input().split())) for _ in range(V)]
    info.insert(0, ['0'])


    V_info = [0] * (V + 1)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    for i in range(1, V + 1):
        V_info[i] = info[i][1]
        if len(info[i]) == 3:
            ch1[i] = int(info[i][2])
        elif len(info[i]) == 4:
            ch1[i] = int(info[i][2])
            ch2[i] = int(info[i][3])

    result = ''
    in_order(1)
    print(f'#{test_case} {result}')