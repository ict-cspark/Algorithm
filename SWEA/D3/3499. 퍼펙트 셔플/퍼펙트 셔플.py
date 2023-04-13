T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    words = list(map(str, input().split()))

    center = (N+1)//2   # center에 중간값 대입

    result = ''
    for i in range(center):
        result += words[i] + ' '
        if center + i < N:
            result += words[center + i] + ' '

    print(f'#{test_case} {result}')