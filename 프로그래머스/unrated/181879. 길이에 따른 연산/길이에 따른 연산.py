def solution(num_list):
    len_list = len(num_list)
    if len_list > 10:
        answer = sum(num_list)
    else:
        answer = 1
        for num in num_list:
            answer *= num
    return answer