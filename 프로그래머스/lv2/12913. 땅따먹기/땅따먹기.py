def solution(land):
    for r in range(1, len(land)):
        for c in range(len(land[0])):
            land[r][c] += max(land[r - 1][0 : c] + land[r - 1][c + 1 : ])
            
    answer = max(land[-1])
    return answer