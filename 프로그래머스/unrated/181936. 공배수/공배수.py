def solution(number, n, m):
    if number % n or number % m:
        answer = 0
    else:
        answer = 1
    return answer