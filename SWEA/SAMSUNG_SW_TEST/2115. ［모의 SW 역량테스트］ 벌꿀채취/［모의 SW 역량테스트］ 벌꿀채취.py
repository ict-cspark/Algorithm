def DFS(K, cnt, S, arr):
    global answer

    if K == M:
        if cnt <= C and answer < S:
            answer = S
            return
    else:
        DFS(K + 1, cnt, S, arr)
        DFS(K + 1, cnt + arr[K], S + (arr[K] ** 2), arr)

    return


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(0, (N - M) + 1):
            answer = 0
            DFS(0, 0, 0, honey[i][j:j + M])
            ans1 = answer

            for ii in range(i, N):
                sj = 0
                if i == ii:
                    sj = j + M
                for jj in range(sj, (N - M) + 1):
                    answer = 0
                    DFS(0, 0, 0, honey[ii][jj:jj + M])
                    ans2 = answer
                    if result < ans1 + ans2:
                        result = ans1 + ans2

    print(f'#{test_case} {result}')