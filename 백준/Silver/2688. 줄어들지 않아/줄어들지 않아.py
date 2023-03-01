import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    result = [1] * 10

    for _ in range(n - 1):
        for i in range(10):
            result[i] = sum(result[i:])

    print(sum(result))