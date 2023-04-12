def solution(board):
    score = 0
    
    for i in range(len(board)):
        if 1 in board[i] and score == 0:
            score = 1
        if i == 0:
            continue

        for j in range(1,len(board[0])):
            if board[i][j] != 0:
                board[i][j] += min(board[i-1][j-1],board[i-1][j],board[i][j-1])
            if board[i][j] > score:
                score = board[i][j]

    answer = pow(score,2)
    return answer