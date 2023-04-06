def solution(common):
    da = common[1] - common[0]
    db = common[2] - common[1]
    if 0 in common:
        r = 0
    else:
        r = common[1] / common[0]
    
    if da == db:
        answer = int(common[-1] + da)
    else:
        answer = int(common[-1] * r)
    return answer