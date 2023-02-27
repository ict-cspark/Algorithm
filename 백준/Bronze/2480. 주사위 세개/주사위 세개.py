number = list(map(int, input().split()))
check = list(set(number))

result = 0
if len(check) == 1:
    result = 10000 + (check[0] * 1000)

elif len(check) == 2:
    if number.count(check[0]) == 2:
        result = 1000 + (check[0] * 100)
    else:
        result = 1000 + (check[1] * 100)

elif len(check) == 3:
    result = max(number) * 100

print(result)