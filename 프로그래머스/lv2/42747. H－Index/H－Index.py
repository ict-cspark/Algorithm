def solution(citations):
    answer = 0
    num = len(citations)
    citations.sort()
    for i in range(num):
        if citations[i] >= num - i:
            answer = num - i
            break
    return answer