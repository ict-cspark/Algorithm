def solution(slice, n):
    answer = 0
    for i in range(1, 51):
        piece = slice * i
        if piece >= n:
            answer = i
            break
    return answer