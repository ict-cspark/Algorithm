T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    busstop = [0] * 5001
    for n in range(N):
        A, B = map(int, input().split())
        for stop in range(A, B + 1):
            busstop[stop] += 1

    P = int(input())
    print(f'#{test_case}', end=" ")
    for p in range(P):
        C = int(input())
        print(busstop[C], end=" ")
    print()