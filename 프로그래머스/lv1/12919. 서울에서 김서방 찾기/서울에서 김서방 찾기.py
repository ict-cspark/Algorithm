def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            ans = i
    answer = f'김서방은 {ans}에 있다'
    return answer