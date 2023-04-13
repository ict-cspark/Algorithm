T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    bus = [0] * 1001
    for _ in range(N):
        T, A, B = map(int, input().split())

        if T == 1:
            for a in range(A, B + 1):
                bus[a] += 1
        elif T == 2:
            for b in range(A, B + 1, 2):
                bus[b] += 1

        else:
            for c in range(A, B + 1):
                if A%2 == 0 and c%4 == 0:
                    bus[c] += 1
                elif A%2 == 1 and c%3 == 0 and c%10 != 0:
                    bus[c] += 1

    print(f'#{test_case} {max(bus)}')