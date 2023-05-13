def solution(s):
    alph = dict()
    answer = []
    for i in range(len(s)):
        if s[i] in alph:
            answer.append(i - alph[s[i]])
            alph[s[i]] = i
        else:
            answer.append(-1)
            alph[s[i]] = i
    return answer