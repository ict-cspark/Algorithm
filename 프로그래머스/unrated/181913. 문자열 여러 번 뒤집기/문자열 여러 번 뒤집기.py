def solution(my_string, queries):
    word = list(my_string)

    for s, e in queries:
        if s > 0:
            word[s : e + 1] = word[e : s - 1 : -1]
        else:
            word[s : e + 1] = word[e :  : -1]
        
    answer = "".join(word)
    return answer