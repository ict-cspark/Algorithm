def solution(my_string, is_prefix):
    answer = 0
    for i in range(1, len(my_string) + 1):
        word = my_string[:i]
        if is_prefix == word:
            answer = 1
            break

    return answer