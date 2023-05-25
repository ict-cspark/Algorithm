def solution(n, a, b):
    answer = 0
    while True:
        if a == b:
            break
        else:
            answer += 1
            a = (a // 2) + (a % 2)
            b = (b // 2) + (b % 2)

    return answer