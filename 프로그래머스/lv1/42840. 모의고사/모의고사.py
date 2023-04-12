def solution(answers):
    answer = []
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    aa = 0
    bb = 0
    cc = 0
    for i in range(len(answers)):
        if answers[i] == a[i]:
            aa = aa+1
        if answers[i] == b[i]:
            bb = bb+1
        if answers[i] == c[i]:
            cc = cc+1
    if aa == max(aa,bb,cc):
        answer.append(1)
    if bb == max(aa, bb, cc):
        answer.append(2)
    if cc == max(aa,bb,cc):
        answer.append(3)
    return answer