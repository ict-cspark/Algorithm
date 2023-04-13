def DFS(k, S):
    global result

    if result >= S:
        return

    if k == N:
        if result < S:
            result = S
        return

    else:
        for i in range(N):
            if check[i] == 0:
                check[i] = 1
                DFS(k + 1, S * (member[k][i]/100))
                check[i] = 0


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    member = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    check = [0] * N
    DFS(0, 1)

    print(f'#{test_case} {(result * 100):.6f}')