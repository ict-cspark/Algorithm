def solution(numLog):
    ctl = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    
    answer = ''
    for i in range(1, len(numLog)):
        num = numLog[i] - numLog[i - 1]
        answer += ctl[num]

    return answer