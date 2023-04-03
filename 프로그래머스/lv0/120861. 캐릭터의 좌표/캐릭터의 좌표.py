delta = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}

def solution(keyinput, board):
    N = board[0] // 2
    M = board[1] // 2
    answer = [0, 0]
    for key in keyinput:
        r = answer[0] + delta[key][0]
        c = answer[1] + delta[key][1]
        if -N <= r <= N:
            answer[0] = r
        if -M <= c <= M:
            answer[1] = c
    
    return answer