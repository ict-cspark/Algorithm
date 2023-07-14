N = int(input())
speed = list(map(int, input().split()))

speed = speed[::-1]
result = 0
for i in range(N):
    if result <= speed[i]:
        result = speed[i]
    else:
        if result % speed[i]:
            result = ((result // speed[i]) + 1) * speed[i]

print(result)