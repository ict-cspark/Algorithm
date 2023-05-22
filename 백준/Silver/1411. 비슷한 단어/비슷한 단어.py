import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())

words = dict()
for _ in range(N):
    word = list(input().strip())

    idx = 1
    for i in range(len(word)):
        s = word[i]

        if s.isdigit():
            continue
        else:
            for j in range(i, len(word)):
                if word[j] == s:
                    word[j] = str(idx)
        idx += 1

    answer = "".join(word)

    if answer in words:
        words[answer] += 1
    else:
        words[answer] = 1

result = 0
for value in words.values():
    result += len(list(combinations(range(value), 2)))

print(result)