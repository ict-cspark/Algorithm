def solution(s):
    round_sum = 0
    for i in s:
        if i == '(':
            round_sum += 1
        elif i == ')':
            round_sum -= 1
        if round_sum < 0:
            break

    if round_sum == 0:
        answer = True
    else:
        answer = False

    return answer