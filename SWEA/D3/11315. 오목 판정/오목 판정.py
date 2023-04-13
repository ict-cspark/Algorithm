def check(go, N):
    dr = [0, 1, 1, 1] # 오른쪽, 아래, 왼쪽 아래 대각선, 오른쪽 아래 대각선
    dc = [1, 0, -1, 1]

    for r in range(N):
        for c in range(N):
            if go[r][c] == 'o':
                for d in range(4):
                    count = 0
                    nr = r
                    nc = c
                    for _ in range(5):
                        if 0 <= nr < N and 0 <= nc < N and go[nr][nc] == 'o':
                            count += 1
                            nr += dr[d]
                            nc += dc[d]

                    if count == 5:
                        return 'YES'
    return 'NO'

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    go = [input() for _ in range(N)]
    result = check(go, N)

    print(f'#{test_case} {result}')