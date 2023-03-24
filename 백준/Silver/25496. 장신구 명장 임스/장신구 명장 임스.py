N, P = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

result = 0
for a in A:
    if N < 200:
        N += a
        result += 1
    else:
        break

print(result)