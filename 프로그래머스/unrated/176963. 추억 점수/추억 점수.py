def solution(name, yearning, photo):
    
    score = dict()
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    answer = []
    for one in photo:
        result = 0
        for o in one:
            result += score.get(o, 0)
        answer.append(result)
        
    return answer