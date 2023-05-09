delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution(n):
    answer = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    
    num = 2
    d = 0
    r, c = 0, 0
    answer[r][c] = 1
    visited[r][c] = 1
    while num <= n ** 2:
        nr = r + delta[d][0]
        nc = c + delta[d][1]
        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            answer[nr][nc] = num
            num += 1
            r = nr
            c = nc
        else:
            d = (d + 1) % 4
        
    return answer