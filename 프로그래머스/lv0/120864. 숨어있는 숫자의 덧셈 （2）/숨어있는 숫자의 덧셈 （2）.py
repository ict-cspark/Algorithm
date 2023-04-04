import re

def solution(my_string):
    my_string = re.sub("[A-Za-z]", " ", my_string)
    my_list = list(map(str, my_string.split()))
    
    answer = 0
    for s in my_list:
        answer += int(s)
        
    return answer