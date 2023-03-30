def solution(order):
    game = ['3', '6', '9']
    
    answer = 0
    for o in str(order):
        if o in game:
            answer += 1
            
    return answer