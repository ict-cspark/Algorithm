def solution(dots):
    R = []
    C = []
    for r, c in dots:
        R.append(r)
        C.append(c)
        
    answer = (max(R) - min(R)) * (max(C) - min(C))
    return answer