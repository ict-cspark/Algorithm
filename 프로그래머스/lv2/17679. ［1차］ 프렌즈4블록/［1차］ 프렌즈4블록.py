def solution(m, n, board):
    friends = []
    for b in board:
        friends.append(list(b))

    answer = 0
    while True:

        cnt = 0
        visited = [[0] * n for _ in range(m)]
        for r in range(m - 1):
            for c in range(n - 1):
                if friends[r][c] != '' and friends[r][c] == friends[r + 1][c] == friends[r][c + 1] == friends[r + 1][c + 1]:
                    visited[r][c], visited[r + 1][c],  visited[r][c + 1],  visited[r + 1][c + 1] = 1, 1, 1, 1
                    cnt += 1

        if cnt == 0:
            break

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 1:
                    friends[i][j] = ''
                    answer += 1

        for i in range(m - 1, 0, -1):
            for j in range(n):
                if friends[i][j] == '':
                    start = i - 1
                    while start >= 0:
                        if friends[start][j] != '':
                            friends[i][j], friends[start][j] = friends[start][j], friends[i][j]
                            break
                        else:
                            start -= 1

    return answer