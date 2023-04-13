delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def DFS(n, r, c, num):
    if n == 7:
        result.add(num)
        return

    for dr, dc in delta:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            DFS(n+1, nr, nc, num*10 + arr[nr][nc])


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()

    for r in range(4):
        for c in range(4):
            DFS(0, r, c, 0)

    print(f'#{test_case} {len(result)}')