import sys
from itertools import combinations
input = sys.stdin.readline

words = [input().strip() for _ in range(3)]
k = int(input())

temp = []
result = set()
for word in words:
    for w in combinations(word, k):
        answer = "".join(w)
        if answer in temp:
            result.add(answer)
        else:
            temp.append(answer)

result = sorted(list(result))
if result:
    for r in result:
        print(r)
else:
    print(-1)