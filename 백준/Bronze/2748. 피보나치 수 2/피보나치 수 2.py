N = int(input())

a = 0
b = 1

for i in range(2, N):
    temp = a + b
    a = b
    b = temp

if N < 2:
    print(N)
else:
    print(a + b)