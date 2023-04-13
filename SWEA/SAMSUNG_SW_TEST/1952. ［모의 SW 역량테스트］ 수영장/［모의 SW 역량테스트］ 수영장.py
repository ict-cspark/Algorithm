def DFS(n, answer):
    global result
    if n > 12:
        if result > answer:
            result = answer
        return

    DFS(n + 1, answer + (plan[n] * d))
    DFS(n + 1, answer + m)
    DFS(n + 3, answer + t)
    DFS(n + 12, answer + y)


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    d, m, t, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    result = 987654321
    DFS(1, 0)

    print(f'#{test_case} {result}')