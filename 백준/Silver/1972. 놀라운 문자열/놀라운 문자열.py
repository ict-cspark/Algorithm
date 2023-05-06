import sys
input = sys.stdin.readline


def value(word):
    l = len(word)

    if l < 3:
        print(f'{word} is surprising.')
        return
    else:
        for i in range(l - 1):
            answer = []
            for j in range(l - i - 1):
                a = word[j] + word[j + (i + 1)]
                if a in answer:
                    print(f'{word} is NOT surprising.')
                    return
                else:
                    answer.append(a)
        else:
            print(f'{word} is surprising.')
            return


while True:
    S = input().strip()
    if S == '*':
        break
    else:
        value(S)