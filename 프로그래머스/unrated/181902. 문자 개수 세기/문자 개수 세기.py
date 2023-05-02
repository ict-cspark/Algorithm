def solution(my_string):
    answer = [0] * 58
    
    for s in my_string:
        answer[ord(s) - 65] += 1
        
    answer = answer[:26] + answer[32:]
    return answer