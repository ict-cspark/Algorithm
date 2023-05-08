def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        pic = picture[i]
        
        result = ''
        for p in pic:
            result += p * k
        
        for _ in range(k):
            answer.append(result)
        
    return answer