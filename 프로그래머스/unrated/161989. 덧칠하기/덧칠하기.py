def solution(n, m, section):
    walls = [0] * (n + 1)
    
    for s in section:
        walls[s] = 1
        
    answer = 0
    for i in range(len(section)):
        start = section[i]
        if walls[start]:
            answer += 1
            for j in range(start, min(start + m, n + 1)):
                walls[j] = 0
        
    return answer