def solution(a, b, n):
    answer = 0
    while n >= a:
        coke = (n // a) * b
        answer += coke
        n = (n % a) + coke
    return answer