delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def solution(board):
    N = len(board)
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                for d in range(8):
                    nr = r + delta[d][0]
                    nc = c + delta[d][1]
                    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 1:
                        board[nr][nc] = -1
                        
    answer = 0
    for b in board:
        answer += b.count(0)
    return answer