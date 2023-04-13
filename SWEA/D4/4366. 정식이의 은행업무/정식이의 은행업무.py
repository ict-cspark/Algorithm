def solve(num2, num3):
    num3 = num3[::-1]
    
    for i in range(len(num2)):
        n2 = num2[:]
        n2[i] = (num2[i] + 1) % 2

        d = 0
        for j in range(len(n2)):
            d = (d * 2) + n2[j]
        answer = d

        n3 = []
        while d > 0:
            n3.append(d % 3)
            d = d//3

        cnt = abs(len(n3) - len(num3))
        for k in range(min(len(n3), len(num3))):
            if n3[k] != num3[k]:
                cnt += 1
        if cnt == 1:
            return answer

    return False


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    num2 = list(map(int, input()))
    num3 = list(map(int, input()))

    result = solve(num2, num3)

    print(f'#{test_case} {result}')