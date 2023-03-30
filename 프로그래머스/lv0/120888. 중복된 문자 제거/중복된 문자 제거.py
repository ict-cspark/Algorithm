def solution(my_string):
    my_string = list(my_string)

    result = []
    for s in my_string:
        if s not in result:
            result.append(s)
    
    answer = "".join(result)
    return answer