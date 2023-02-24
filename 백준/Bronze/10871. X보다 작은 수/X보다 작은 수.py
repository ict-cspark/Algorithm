N, X =  map(int, input().split(' '))
A = list(map(int, input().split(' ')))

result = []
for i in A:
    if i < X:
        result.append(str(i))
total = " ".join(result)
print(total)