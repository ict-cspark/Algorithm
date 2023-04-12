def solution(s):
    answer = []
    s = s.lower()
    words = s.split(' ')
    for word in words:
        if word == '':
            answer.append(word)
        elif word[0].isdecimal():
            answer.append(word)
        else:
            word = word.capitalize()
            answer.append(word)

    answer = ' '.join(answer)
    return answer