import sys
input = sys.stdin.readline


def word_trans(w):
    if len(w) > 2:
        wm = sorted(w[1:-1])
        w = w[0] + "-" + w[-1] + "-" + "".join(wm)
    elif len(w) == 2:
        w = w[0] + "-" + w[1]
    return w


N = int(input())

words = dict()
for _ in range(N):
    word = input().strip()
    new_word = word_trans(word)

    if new_word not in words:
        words[new_word] = word

M = int(input())
words_s = list(input().split())

for i in range(M):
    answer = word_trans(words_s[i])
    words_s[i] = words[answer]

result = " ".join(words_s)
print(result)