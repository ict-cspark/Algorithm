num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def solution(my_string):
    answer = 0
    
    for ms in my_string:
        if ms in num:
            answer += int(ms)
            
    return answer