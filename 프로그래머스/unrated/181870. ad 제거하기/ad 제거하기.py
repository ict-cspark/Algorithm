def solution(strArr):
    answer = []
    for word in strArr:
        if not 'ad' in word:
            answer.append(word)
    return answer