def DFS(K, a, b):
    global result

    if len(a) > N // 2:
        return
    if K == N:
        if len(a) == len(b):
            asum = 0
            bsum = 0
            for i in range(len(a)):
                for j in range(len(a)):
                    asum += food[a[i]][a[j]]
                    bsum += food[b[i]][b[j]]
            answer = abs(asum - bsum)
            if result > answer:
                result = answer
        return
    else:
        DFS(K + 1, a + [K], b)
        DFS(K + 1, a, b + [K])


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]

    result = 987654321
    DFS(0, [], [])

    print(f'#{test_case} {result}')