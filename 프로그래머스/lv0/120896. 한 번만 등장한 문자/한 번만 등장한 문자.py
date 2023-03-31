def solution(s):
    S = list(s)
    words = {}
    for s in S:
        if s in words:
            words[s] += 1
        else:
            words[s] = 1
            
    words = sorted(words.items())
    answer = ""
    for word in words:
        if word[1] == 1:
            answer += word[0]
            
    return answer