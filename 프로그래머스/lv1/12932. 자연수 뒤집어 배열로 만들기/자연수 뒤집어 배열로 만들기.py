import copy
def solution(n):
    answer = []
    a = 0
    while n>0:
        a = n%10
        answer += [a]
        n = int(n/10)
    return answer