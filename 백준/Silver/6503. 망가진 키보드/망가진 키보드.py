import sys
input = sys.stdin.readline

while True:
    M = int(input())
    if M == 0:
        break
    words = input().strip()

    N = len(words)
    M_dic = dict()
    M_dic[words[0]] = 1

    result = 0
    left = 0
    right = 0
    while right < N:
        if len(M_dic) <= M:
            result = max(result, right - left + 1)
            right += 1
            if right < N:
                alph = words[right]
                if alph in M_dic:
                    M_dic[alph] += 1
                else:
                    M_dic[alph] = 1

        else:
            alph = words[left]
            M_dic[alph] -= 1
            if M_dic[alph] == 0:
                del M_dic[alph]
            left += 1

    print(result)