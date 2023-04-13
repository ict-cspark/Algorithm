def fast_check(arr):
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append([i, j])
    result = 0
    for sr in range(N):
        for sc in range(N):
            cnt = [0] * ((2 * N) + 1)
            for r, c in home:
                idx = abs(sr - r) + abs(sc - c) + 1
                cnt[idx] += 1
            compare = cnt[:]
            for i in range(1, len(cnt)):
                compare[i] = compare[i] + compare[i - 1]

            for j in range(1, len(compare)):
                if cost[j] <= compare[j] * M and result < compare[j]:
                    result = compare[j]

    return result


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    cost = [0] + [((K * K) + ((K - 1) * (K - 1))) for K in range(1, (2 * N) + 1)]

    result = fast_check(city)

    print(f'#{test_case} {result}')