def solution(word):
    answer = 0
    word_idx = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}

    for i in range(len(word)):
        answer += ((5 ** (5 - i) // 4) * word_idx[word[i]] + 1)
    return answer