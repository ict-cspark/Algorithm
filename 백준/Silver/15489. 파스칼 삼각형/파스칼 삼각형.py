R, C, W = map(int, input().split())

pascal = [[], [1], [1, 1]]
for i in range(3, R + W):
    answer = [1]
    for j in range(1, i - 1):
        temp = pascal[i - 1][j - 1] + pascal[i - 1][j]
        answer.append(temp)
    answer.append(1)
    pascal.append(answer)

result = 0
k = 1
for r in range(R, R + W):
    for c in range(k):
        result += pascal[r][C - 1 + c]
    k += 1

print(result)