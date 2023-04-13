# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    # 날짜 N 입력받고 매매가는 리스트로 변환해서 입력받기
    N = int(input())
    arr = list(map(int, input().split()))

    arr_max = arr[N - 1]
    result = 0
    for i in range(N - 2, -1, -1):
        if arr_max > arr[i]:
            result += arr_max - arr[i]
        else:
            arr_max = arr[i]

    print(f'#{test_case} {result}')