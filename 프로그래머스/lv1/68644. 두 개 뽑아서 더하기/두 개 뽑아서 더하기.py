import itertools

def solution(numbers):
    num = list(itertools.combinations(numbers, 2))
    
    result = []
    for a, b  in num:
        result.append(a + b)
    
    result = list(set(result))
    answer = sorted(result)
    return answer