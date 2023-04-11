X = int(input())

last = 0

for i in range(X):
    last += i+1
    if last >= X:
        order = i+1
        break

if order%2 == 0:
    base = order-(last-X)
    result = str(base) + '/' + str((order+1)-base)
else:
    base = 1 + (last-X)
    result = str(base) + '/' + str((order+1)-base)

print(result)