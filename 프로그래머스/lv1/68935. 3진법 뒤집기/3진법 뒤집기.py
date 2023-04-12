def solution(n):
    reverse = ''
    while n >= 1:
        reverse = reverse + str(n % 3)
        n = n // 3
    answer = int(reverse,3)
    return answer