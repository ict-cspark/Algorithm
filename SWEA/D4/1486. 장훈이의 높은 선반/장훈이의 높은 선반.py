def DFS(K, S):
    global result
    if S - B >= result:
        return
    if K == N:
        if S >= B:
            answer = S - B
            if result > answer:
                result = answer
        return
    else:
        P[K] = 0
        DFS(K + 1, S)
        P[K] = 1
        DFS(K + 1, S + H[K])

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    P = [0] * N

    result = 987654321
    DFS(0, 0)

    print(f'#{test_case} {result}')