def solution(my_string):
    my_string = list(map(str, my_string.split()))
    answer = int(my_string[0])
    for i in range(2, len(my_string)):
        if my_string[i] != '+' and my_string[i] != '-':
            if my_string[i - 1] == '+':
                answer += int(my_string[i])
            elif my_string[i - 1] == '-':
                answer -= int(my_string[i])

    return answer