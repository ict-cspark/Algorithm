def solution(n, words):
    words = [words[0][0]] + words

    turn = 0
    num = 0
    words_dic = dict()
    words_dic[words[0][0]] = words[0][0]
    for i in range(1, len(words), n):
        if num != 0:
            break
        else:
            turn += 1
            for j in range(i, i + n):
                if words[j - 1][-1] == words[j][0] and words[j] not in words_dic:
                    words_dic[words[j]] = words[j][-1]
                else:
                    num = ((j - 1) % n) + 1
                    break

    if num == 0:
        turn = 0

    answer = [num, turn]
    return answer