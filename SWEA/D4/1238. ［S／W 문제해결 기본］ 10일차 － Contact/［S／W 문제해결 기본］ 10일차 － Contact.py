def BFS(S):
    visit = [0] * 101
    queue = [S]

    visit[S] = 1
    answer = S
    while queue:
        r = queue.pop(0)
        if visit[answer] < visit[r] or visit[answer] == visit[r] and answer < r:
            answer = r

        for c in range(101):
            if arr[r][c] and visit[c] == 0:
                queue.append(c)
                visit[c] = visit[r] + 1
    return answer

# 테스트케이스 입력받기
T = 10

for test_case in range(1, T + 1):
    N, S = map(int, input().split())
    num = list(map(int, input().split()))

    arr = [[0] * 101 for _ in range(101)]

    for n in range(0, N, 2):
        arr[num[n]][num[n + 1]] = 1

    result = BFS(S)

    print(f'#{test_case} {result}')