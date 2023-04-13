T = int(input())

for t in range(1, T + 1):
    A, B = map(str, input().split())

    A_new = A.replace(B, '*')
    result = len(A_new)

    print(f'#{t} {result}')