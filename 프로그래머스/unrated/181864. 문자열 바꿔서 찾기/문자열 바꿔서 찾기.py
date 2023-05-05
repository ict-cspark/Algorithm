def solution(myString, pat):
    word = ""
    for alph in myString:
        if alph == 'A':
            word += 'B'
        else:
            word += 'A'
    
    if pat in word:
        answer = 1
    else:
        answer = 0
    return answer