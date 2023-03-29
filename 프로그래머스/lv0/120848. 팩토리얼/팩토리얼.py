def solution(n):
    answer = 1
    result = 1
    while True:
        if result > n:
            answer -= 1
            break
        else:
            answer += 1
            result *= answer
            
    return answer