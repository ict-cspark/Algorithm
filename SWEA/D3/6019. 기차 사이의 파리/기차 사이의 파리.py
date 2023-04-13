# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    
    sol = D / (A + B)
    result = sol * F

    print(f'#{test_case} {result:0.10F}')