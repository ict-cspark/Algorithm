T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    num = []
    for _ in range(N):
        num += [list(map(int, input().split()))]

    num_90 = [[0] * N for _ in range(N)]
    num_180 = [[0] * N for _ in range(N)]
    num_270 = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            num_90[r][c] = num[N - c -1][r]
            num_180[r][c] = num[N - r - 1][N - c -1]
            num_270[r][c] = num[c][N - r - 1]

    print(f'#{test_case}')
    for i in range(N):
        print("".join(map(str, num_90[i])),end=" ")
        print("".join(map(str, num_180[i])),end=" ")
        print("".join(map(str, num_270[i])))