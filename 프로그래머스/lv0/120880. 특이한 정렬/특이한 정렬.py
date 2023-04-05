def solution(numlist, n):
    numlist.sort()
    N = len(numlist)
    
    valuelist = []
    for i in range(N):
        valuelist.append([abs(numlist[i] - n), numlist[i]])   
    
    valuelist = sorted(valuelist, key = lambda x:(x[0], -x[1]))

    answer = []
    for j in range(N):
        answer.append(valuelist[j][1])
    return answer