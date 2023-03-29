num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def solution(my_string):
    my_string = list(my_string)

    answer = []
    for ms in my_string:
        if ms in num:
            answer.append(int(ms))
            
    answer.sort()
    return answer