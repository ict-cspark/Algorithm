# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    # 배열 길이 N과 파리채 길이 M 입력 받기
    N, M = map(int, input().split())
    # MxM 2차원 행렬 만들어서 입력 받기
    arr = []
    for n in range(N):
        arr += [list(map(int, input().split()))]

    max_arr = 0
    for r in range((N - M) + 1):
        for c in range((N - M) + 1):
            bugs = 0
            for rm in range(M):
                for cm in range(M):
                    bugs += arr[r + rm][c + cm]
            if max_arr < bugs:
                max_arr = bugs

    print(f'#{test_case} {max_arr}')