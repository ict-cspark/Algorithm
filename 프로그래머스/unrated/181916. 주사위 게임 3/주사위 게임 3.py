def solution(a, b, c, d):
    arr = [a, b, c, d]
    temp = list(set(arr))
    cnt = len(temp)
    
    answer = 0
    if cnt == 1:
        answer = 1111 * temp[0]
    elif cnt == 2:
        if arr.count(temp[0]) == 2:
            answer = (temp[0] + temp[1]) * abs(temp[0] - temp[1])
        else:
            if arr.count(temp[0]) == 3:
                answer = ((10 * temp[0]) + temp[1]) ** 2
            else:
                answer = ((10 * temp[1]) + temp[0]) ** 2
    elif cnt == 3:
        if arr.count(temp[0]) == 2:
            answer = temp[1] * temp[2]
        elif arr.count(temp[1]) == 2:
            answer = temp[0] * temp[2]
        else:
            answer = temp[0] * temp[1]
    else:
        answer = min(temp)
    
    return answer