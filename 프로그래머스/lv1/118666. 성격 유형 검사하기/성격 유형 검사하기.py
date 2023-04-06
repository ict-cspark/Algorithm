indicator = [{'R': 0, 'T': 0}, {'C': 0, 'F': 0}, {'J': 0, 'M': 0}, {'A': 0, 'N': 0}]

def solution(survey, choices):
    
    for i in range(len(survey)):
        score = choices[i]
        if score < 4:
            score = 4 - score
            character = survey[i][0]
        elif score > 4:
            score = score % 4
            character = survey[i][1]
        else:
            continue
            
        for j in range(4):
            if character in indicator[j]:
                indicator[j][character] += score
                break
                         
    for k in range(4):
        indicator[k] = sorted(indicator[k].items(), key = lambda x: (-x[1], x[0]))
    
    answer = ""
    for l in range(4):
        answer += indicator[l][0][0]
    return answer