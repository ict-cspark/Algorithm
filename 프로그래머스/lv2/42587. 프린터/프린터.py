def solution(priorities, location):
    result = []
    for idx, order in enumerate(priorities):
        result.append((order, idx))

    answer = []
    while result:
        res = result[0]
        res_max = max(result)
        if res[0] != res_max[0]:
            temp = result.pop(0)
            result.append(temp)
        else:
            temp = result.pop(0)
            answer.append(temp)


    for loc in range(len(answer)):
        if answer[loc][1] == location:
            break
    return loc + 1