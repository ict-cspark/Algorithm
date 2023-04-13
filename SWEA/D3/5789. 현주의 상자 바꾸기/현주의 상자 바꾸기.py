# 테스트케이스 입력 받기
T = int(input())
for test_case in range(1, T + 1):
    # 리스트 길이 N과 반복횟수 Q 입력받기
    N, Q = map(int, input().split())

    # 0으로 채워진 길이 N 리스트 생성
    arr = [0] * N

    # Q 만큼 반복문을 실행하여 L, R 입력받기
    for i in range(1, Q + 1):
        L, R = map(int, input().split())

        # L ~ R 인덱스 만큼 arr 리스트에 i로 채우기
        for j in range(L - 1, R):
            arr[j] = i

    # 결과를 문자열로 출력
    result = " ".join(map(str, arr))
    print(f'#{test_case} {result}')