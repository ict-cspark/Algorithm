def solution(emergency):
    emergency_new = sorted(emergency, reverse=True)
    
    answer = []
    for e in emergency:
        temp = emergency_new.index(e)
        answer.append(temp + 1)
        
    return answer