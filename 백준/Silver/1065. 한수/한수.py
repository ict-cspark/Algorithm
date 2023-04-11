N = int(input())
count = 99
if N <= 99:
    count = N

for i in range(100,N+1):
    i = str(i)
    if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
        count += 1

print(count)