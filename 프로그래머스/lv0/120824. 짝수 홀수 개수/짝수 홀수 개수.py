def solution(num_list):
    even = 0
    odd = 0
    for n in num_list:
        if n % 2:
            odd += 1
        else:
            even += 1
    
    answer = [even, odd]
    return answer