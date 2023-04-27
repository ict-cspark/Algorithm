def solution(num_list):
    a = 1
    b = sum(num_list) ** 2
    for num in num_list:
        a *= num
        
    if a < b:
        answer = 1
    else:
        answer = 0
    return answer