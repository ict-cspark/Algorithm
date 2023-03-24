def solution(n):
    pizza = n // 7
    if n % 7:
        pizza += 1
    answer = pizza
    return answer