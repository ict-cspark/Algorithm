def solution(my_string):
    answer = []
    for i in range(len(my_string) - 1, -1, -1):
        word = my_string[i : ]
        answer.append(word)
    answer.sort()
    return answer