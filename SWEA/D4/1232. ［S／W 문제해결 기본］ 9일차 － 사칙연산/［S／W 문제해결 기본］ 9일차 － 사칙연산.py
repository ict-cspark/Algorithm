def ca(first, second, op):
    if op == '+':
        return first + second
    elif op == '-':
        return first - second
    elif op == '*':
        return first * second
    elif op == '/':
        return first / second

def chg_type(char):
    if char.isnumeric():
        return int(char)
    else:
        return char

# 테스트케이스 입력받기
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    info = [list(map(chg_type, input().split())) for _ in range(N)]

    calc = ['+', '-', '*', '/']
    tree = [0] * (N + 1)

    for n in range(N):
        t = n + 1
        if info[n][1] in calc:
            tree[t] = info[n][1]
        else:
            tree[t] = info[n][1]


    for t in range(N, 0, -1):
        if tree[t] in calc:
            first = tree[info[t - 1][2]]
            second = tree[info[t - 1][3]]
            op = tree[t]
            answer = ca(first, second, op)
            tree[t] = answer

    result = int(tree[1])
    print(f'#{test_case} {result}')