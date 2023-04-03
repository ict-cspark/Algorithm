def solution(numbers):
    numbers.sort()

    a = numbers[0] * numbers[1]
    b = numbers[-2] * numbers[-1]
    if a > b:
        answer = a
    else:
        answer = b
        
    return answer