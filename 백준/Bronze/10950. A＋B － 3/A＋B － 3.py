num = int(input())
for i in range(num):
    result = list(map(int, input().split(' ')))
    total = result[0] + result[1] 
    print(total)