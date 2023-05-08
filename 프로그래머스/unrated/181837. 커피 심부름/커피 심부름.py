def solution(order):
    answer = 0
    for menu in order:
        if 'americano' in menu:
            answer += 4500
        elif 'cafelatte' in menu:
            answer += 5000
        elif 'anything' in menu:
            answer += 4500
    return answer