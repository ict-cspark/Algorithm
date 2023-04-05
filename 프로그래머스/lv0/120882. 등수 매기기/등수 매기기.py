def solution(score):
    N = len(score)

    ranking = []
    for i in range(N):
        avg = sum(score[i]) / 2
        ranking.append([avg, i])
        
    ranking.sort(reverse=True)
    
    answer = [0] * N
    val = 0
    idx = 1
    for j in range(N):
        if ranking[j][0] != val:
            val = ranking[j][0]
            idx = j + 1
            answer[ranking[j][1]] = idx

        else:
            answer[ranking[j][1]] = idx
            
    return answer