vow = ['a', 'e', 'i', 'o', 'u']

def solution(my_string):
    my_string = list(my_string)
    
    answer = ''
    for ms in my_string:
        if ms not in vow:
            answer += ms
    
    return answer