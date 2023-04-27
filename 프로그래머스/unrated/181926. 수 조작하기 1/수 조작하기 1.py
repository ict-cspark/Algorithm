def solution(n, control):
    ctl = { 'w': 1, 's': -1, 'd': 10, 'a': -10 }
    answer = n
    for c in control:
        answer += ctl[c]
    return answer