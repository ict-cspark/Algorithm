def solution(park, routes):
    delta = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    R = len(park)
    C = len(park[0])
    park_map = [[0] * C for _ in range(R)]

    sr = 0
    sc = 0
    for i in range(R):
        for j in range(C):
            if park[i][j] == "S":
                park_map[i][j] = 1
                sr = i
                sc = j
            elif park[i][j] == "X":
                park_map[i][j] = -1

    for route in routes:
        d, k = route.split()

        r = sr
        c = sc
        for t in range(int(k)):
            nr = r + delta[d][0]
            nc = c + delta[d][1]

            if 0 <= nr < R and 0 <= nc < C and park_map[nr][nc] != -1 :
                r = nr
                c = nc
            else:
                break
        else:
            sr = r
            sc = c

    answer = [sr, sc]
    return answer
