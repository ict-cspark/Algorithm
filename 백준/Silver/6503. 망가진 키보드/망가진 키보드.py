import sys
input = sys.stdin.readline

while True:
    M = int(input())
    if M == 0:
        break
    sentence = input().strip()
    N = len(sentence)

    result = 0
    M_dic = dict()
    M_dic[sentence[0]] = 1

    left = 0
    right = 0
    while right < N:
        if len(M_dic) <= M:
            result = max(result, right - left + 1)
            right += 1
            if right < N:
                alph = sentence[right]
                if alph in M_dic:
                    M_dic[alph] += 1
                else:
                    M_dic[alph] = 1

        else:
            alph = sentence[left]
            if alph in M_dic:
                M_dic[alph] -= 1
                if M_dic[alph] == 0:
                    del M_dic[alph]
                left += 1

    print(result)