def pascal(N):
    if N == 1:
        num = [1]
        return num

    num = pascal(N - 1)
    my_num = [1]

    for i in range(1, N):
        temp = 0
        if i - 1 >= 0:
            temp += num[i - 1]
        if i < N - 1:
            temp += num[i]
        my_num.append(temp)

    return my_num

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    print(f'#{test_case}')
    for n in range(1, N + 1):
        print(" ".join(map(str, pascal(n))))