
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

R = []
C = []
for _ in range(M):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)

R.sort()
C.sort()

middle = M // 2
if M % 2:
    MR = R[middle]
    MC = C[middle]
else:
    MR = (R[middle - 1] + R[middle]) // 2
    MC = (C[middle - 1] + C[middle]) // 2

result = 0
for i in range(M):
    result += abs(MR - R[i]) + abs(MC - C[i])

print(result)