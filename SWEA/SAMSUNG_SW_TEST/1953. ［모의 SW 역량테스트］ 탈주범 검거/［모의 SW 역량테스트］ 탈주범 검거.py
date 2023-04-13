pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
arrive = [1, 0, 3, 2]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(r, c, l): 
    result = 1   
    queue = [(r, c)]    
    visit[r][c] = 1    

    while queue:                
        r, c = queue.pop(0)

        if visit[r][c] == l:      
            return result
        for i in range(4):                                  
            nr = r + delta[i][0]
            nc = c + delta[i][1]
            if 0 <= nr < N and 0 <= nc < M and pipe[t_map[r][c]][i] and pipe[t_map[nr][nc]][arrive[i]] and visit[nr][nc] == 0:
                queue.append((nr, nc))
                visit[nr][nc] = visit[r][c] + 1
                result += 1

    return result

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())            
    t_map = [list(map(int, input().split())) for _ in range(N)] 
    visit = [[0] * M for _ in range(N)]                 

    result = BFS(R, C, L)                             

    print(f'#{test_case} {result}')