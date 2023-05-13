def solution(k, score):
    answer = []
    top = []
    for s in score:
        top.append(s)
        top.sort(reverse=True)
        top = top[:k]
        answer.append(top[-1])
            
    return answer