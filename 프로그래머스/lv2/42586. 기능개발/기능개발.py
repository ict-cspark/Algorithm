import math

def solution(progresses, speeds):
    result = []
    for i in range(len(progresses)):
        temp = (100 - progresses[i]) / speeds[i]
        result.append(math.ceil(temp))

    answer = []
    cnt = 1
    flag = result[0]
    for j in range(1, len(result)):
        if flag < result[j]:
            answer.append(cnt)
            cnt = 1
            flag = result[j]
        else:
            cnt += 1

    answer.append(cnt)
    return answer