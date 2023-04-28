def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        temp = set()
        for s in str(i):
            temp.add(s)
        temp = list(temp)
        if len(temp) > 2:
            continue
        else:
            if '5' in temp or '0' in temp:
                if '5' in temp:
                    temp.remove('5')
                if '0' in temp:
                    temp.remove('0')
                if len(temp) == 0:
                    answer.append(i)
                else:
                    continue
            else:
                continue
                
    if answer == []:
        answer.append(-1)
    return answer