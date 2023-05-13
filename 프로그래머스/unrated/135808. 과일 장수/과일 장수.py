def solution(k, m, score):
    score.sort(reverse=True)

    answer = 0
    for i in range(len(score) // m):
        l = i * m
        answer += min(score[l : l + m]) * m
    return answer