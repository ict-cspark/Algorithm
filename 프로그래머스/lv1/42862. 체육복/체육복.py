def solution(n, lost, reserve):
    nn = []
    lost2 = []
    lost.sort()
    reserve.sort()
    for i in range(1,n+1):
        nn.append(i)
    for i in range(len(lost)):
        nn.remove(lost[i])

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                nn.append(lost[i])
                lost2.append(lost[i])
                del reserve[j]
                break

    for i in range(len(lost2)):
        lost.remove(lost2[i])

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if (lost[i]-1) == reserve[j]:
                nn.append(lost[i])
                del reserve[j]
                break
            elif (lost[i]+1) == reserve[j]:
                nn.append(lost[i])
                del reserve[j]
                break

    answer = len(nn)
    return answer