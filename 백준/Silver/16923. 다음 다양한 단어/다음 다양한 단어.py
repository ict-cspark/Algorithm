S = input()
L = list(S)
N = len(S)

alphabet = [0] * 26

for s in S:
    alphabet[ord(s) - 97] += 1

result = -1
if N < 26:
    idx = alphabet.index(0)
    result = S + chr(idx + 97)
else:
    for i in range(25, 0, -1):
        if L[i] > L[i - 1]:
            answer = sorted(L[i - 1:])
            idx = answer.index(L[i - 1])
            result = S[:i - 1] + answer[idx + 1]
            break

print(result)