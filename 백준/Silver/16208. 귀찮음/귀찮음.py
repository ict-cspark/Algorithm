n = int(input())
A = list(map(int, input().split()))
A.sort()

stick_len = sum(A)
result = 0
for a in A:
    stick_len -= a
    result += a * stick_len

print(result)