N = int(input())
lst = list(map(int,input().split(' ')))
min = lst[0]
max = lst[0]
for i in range(N):
    if lst[i] >= max:
        max = lst[i]
    if lst[i] <= min:
        min = lst[i]
print(min, max)