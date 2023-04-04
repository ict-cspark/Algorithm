def solution(spell, dic):
    answer = 2
    for word in dic:
        for s in spell:
            if s not in word or word.count(s) != 1:
                break
        else:
            answer = 1
            break
                           
    return answer