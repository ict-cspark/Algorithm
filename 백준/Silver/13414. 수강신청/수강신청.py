import sys
input = sys.stdin.readline

K, L = map(int, input().split())

students = dict()
for i in range(L):
    student = input().strip()
    students[student] = i

students = sorted(students.items(), key=lambda x: x[1])

if K > len(students):
    N = len(students)
else:
    N = K

for j in range(N):
    print(students[j][0])