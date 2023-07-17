import sys
input = sys.stdin.readline

while True:
    numbers = list(map(int, input().split()))

    if numbers[0] == 0:
        break
    else:
        numbers = sorted(numbers[1:])
        zero = numbers.count(0)
        numbers = numbers[zero:]

        a = ""
        b = ""
        for i in range(len(numbers)):
            if i % 2 == 0:
                a += str(numbers[i])
            else:
                b += str(numbers[i])

        z_a = zero // 2
        z_b = zero // 2
        if len(a) > len(b):
            z_b += zero % 2
        else:
            z_a += zero % 2

        a = a[0] + ("0" * z_a) + a[1:]
        b = b[0] + ("0" * z_b) + b[1:]

        result = int(a) + int(b)
        print(result)