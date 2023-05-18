import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())

words = dict()
for _ in range(N):
    word = list(input().strip())

    idx = 1
    for i in range(len(word)):
        alph = word[i]

        if alph.isdecimal():
            continue
        else:
            for j in range(i, len(word)):
                if word[j] == alph:
                    word[j] = str(idx)
            idx += 1

    result = "".join(word)
    if result in words:
        words[result] += 1
    else:
        words[result] = 1

answer = 0
for value in words.values():
    answer += len(list(combinations(range(value), 2)))

print(answer)