delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]

def game(sr, sc, color):
    board[sr][sc] = color

    for dr, dc in delta:
        temp = []
        for n in range(1, N):
            nr = sr + (dr * n)
            nc = sc + (dc * n)
            if 0 < nr <= N and 0 < nc <= N and board[nr][nc] != 0 and board[nr][nc] != board[sr][sc]:
                temp.append([nr, nc])
            elif 0 < nr <= N and 0 < nc <= N and board[nr][nc] == board[sr][sc]:
                for r, c in temp:
                    if color == 1:
                        board[r][c] = 1
                    else:
                        board[r][c] = 2
                break
            else:
                break
    return


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    play = [list(map(int, input().split())) for _ in range(M)]

    board = [[0] * (N + 1) for _ in range(N + 1)]
    board[N//2][N//2], board[(N//2) + 1][(N//2) + 1] = 2, 2
    board[N//2][(N//2) + 1], board[(N//2) + 1][N//2] = 1, 1

    for sr, sc, color in play:
        game(sr, sc, color)

    black = 0
    white = 0
    for i in range(N + 1):
        black += board[i].count(1)
        white += board[i].count(2)
    print(f'#{test_case} {black} {white}')