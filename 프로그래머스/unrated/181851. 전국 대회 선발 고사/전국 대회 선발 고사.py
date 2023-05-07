def solution(rank, attendance):
    result = []
    cnt = 0
    for i in range(1, len(rank) + 1):
        if cnt >= 3:
            break
        idx = rank.index(i)
        if attendance[idx]:
            result.append(idx)
            cnt += 1
            
    answer = (10000 * result[0]) + (100 * result[1]) + result[2]
    return answer