def solution(k, tangerine):
    box = dict()
    for t in tangerine:
        if t in box:
            box[t] += 1
        else:
            box[t] = 1
            
    box = list(box.items())
    box = sorted(box, key= lambda x: -x[1])

    answer = 0
    cnt = 0
    for b in box:
        answer += 1
        cnt += b[1]
        if cnt >= k:
            break
            
    return answer