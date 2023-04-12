def solution(N, stages):
    dic = {}
    user = len(stages)
    for i in range(N):
        nopass = 0
        for j in stages:
            if j == (i + 1):
                nopass += 1

        if user != 0:
            fail = nopass / user
            user -= nopass
        else:
            fail = 0
        dic[i + 1] = fail
    answer = sorted(dic, key=lambda x: dic[x], reverse=True)
    return answer