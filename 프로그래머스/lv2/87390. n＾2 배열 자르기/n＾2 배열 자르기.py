def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        value = max(i // n, i % n)
        answer.append(value + 1)
        
    return answer