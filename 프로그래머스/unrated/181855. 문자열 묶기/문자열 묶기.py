def solution(strArr):
    strLen = [0] * 31
    for s in strArr:
        strLen[len(s)] += 1
    answer = max(strLen)
    return answer