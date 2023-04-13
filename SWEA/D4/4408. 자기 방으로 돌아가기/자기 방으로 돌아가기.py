# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    room = [0] * 401
    for _ in range(N):
        A, B = map(int, input().split())
        if A > B:
            A, B = B, A
        if A%2 == 0:
            A = A - 1
        for i in range(A, B + 1):
            room[i] += 1

    result = 0
    for j in range(401):
        if result < room[j]:
            result = room[j]

    print(f'#{test_case} {result}')