def solution(s):
    S = list(map(str, s.split()))
    
    answer = 0
    for i in range(len(S)):
        if S[i] == 'Z':
            answer -= int(S[i - 1])
        else:
            answer += int(S[i])
            
    return answer