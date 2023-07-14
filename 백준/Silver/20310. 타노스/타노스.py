N = input()

even = 0
odd = 0
for n in N:
    if int(n):
        odd += 1
    else:
        even += 1

even = even // 2
odd = odd // 2

result = "0" * even + "1" * odd
print(result)