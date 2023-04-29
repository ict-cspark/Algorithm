import sys
from itertools import combinations
input = sys.stdin.readline

words = [input().strip() for _ in range(3)]
k = int(input())

temp = dict()
result = dict()
for word in words:
    for w in combinations(word, k):
        answer = "".join(w)
        if answer in temp:
            result[answer] = 1
        else:
            temp[answer] = 1


if result:
    result = sorted(result.items())
    for r in result:
        print(r[0])
else:
    print(-1)