def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        string = my_strings[i]
        result = string[parts[i][0] : parts[i][1] + 1]
        answer += result
    return answer