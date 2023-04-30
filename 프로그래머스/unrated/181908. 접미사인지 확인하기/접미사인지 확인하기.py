def solution(my_string, is_suffix):
    words = []
    for i in range(len(my_string) - 1, -1, -1):
        word = my_string[i:]
        words.append(word)
    
    if is_suffix in words:
        answer = 1
    else:
        answer = 0
    return answer