delta = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
switch = [0, 2, 1, 4, 3]


def move(arr):
    for i in range(len(arr)):
        arr[i][0] = arr[i][0] + delta[arr[i][3]][0]
        arr[i][1] = arr[i][1] + delta[arr[i][3]][1]

        if 0 < arr[i][0] < N -1 and 0 < arr[i][1] < N -1:
            continue
        else:
            arr[i][2] = arr[i][2] // 2
            arr[i][3] = switch[arr[i][3]]
    arr.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

    start = 1
    while start < len(arr):
        if arr[start][0] == arr[start - 1][0] and arr[start][1] == arr[start - 1][1]:
            arr[start - 1][2] += arr[start][2]
            arr.pop(start)
        else:
            start += 1

    return


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    group = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        move(group)

    result = 0
    for g in range(len(group)):
        result += group[g][2]
    print(f'#{test_case} {result}')