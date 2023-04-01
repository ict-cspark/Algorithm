def solution(quiz):
    answer = []
    for q in quiz:
        Q = list(map(str, q.split()))
        if Q[1] == '+':
            result = int(Q[0]) + int(Q[2])
        else:
            result = int(Q[0]) - int(Q[2])
            
        if result == int(Q[4]):
            answer.append('O')
        else:
            answer.append('X')
            
    return answer