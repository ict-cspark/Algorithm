result = 0
number = list(map(int, input().split()))

for i in number:
    result += i ** 2

result = result % 10
print(result)