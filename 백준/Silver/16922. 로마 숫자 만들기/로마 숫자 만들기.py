from itertools import combinations_with_replacement

N = int(input())
roma = {"I": 1, "V": 5, "X": 10, "L": 50}

combi = list(combinations_with_replacement(['I', 'V', 'X', 'L'], N))

result = set()
for com in combi:
    answer = 0
    for c in com:
        answer += roma[c]
    result.add(answer)

print(len(result))