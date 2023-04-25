N = int(input())

num = 1
for n in range(N, 0, -1):
    num *= n

num = str(num)
result = 0
for i in range(len(num) - 1, -1, -1):
    if num[i] == '0':
        result += 1
    else:
        break

print(result)