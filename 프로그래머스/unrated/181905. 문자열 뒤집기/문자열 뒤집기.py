def solution(my_string, s, e):
    my_list = list(my_string)
    if s == 0:
        my_list[s : e + 1] = my_list[e : : -1]
    else:
        my_list[s : e + 1] = my_list[e : s - 1 : -1]
    answer = ''.join(my_list)
    return answer