import sys
input = sys.stdin.readline

numbers = [""] * 16
numbers[0] = "{}"
numbers[1] = "{{}}"

for i in range(2, 16):
    numbers[i] = numbers[i - 1][:-1] + "," + numbers[i - 1] + "}"

T = int(input())

for _ in range(T):
    A = input().strip()
    B = input().strip()

    result = numbers.index(A) + numbers.index(B)
    print(numbers[result])