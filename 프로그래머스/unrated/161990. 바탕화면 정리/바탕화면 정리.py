def solution(wallpaper):
    r = len(wallpaper)
    c = len(wallpaper[0])
    
    r_max = 0
    r_min = 50
    c_max = 0
    c_min = 50
    
    for i in range(r):
        for j in range(c):
            if wallpaper[i][j] == '#':
                r_max = max(r_max, i)
                r_min = min(r_min, i)
                c_max = max(c_max, j)
                c_min = min(c_min, j)
                
    answer = [r_min, c_min, r_max + 1, c_max + 1]
    return answer