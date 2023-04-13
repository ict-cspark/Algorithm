# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    # 막대기와 레이저 배치 표현식 입력받기
    sticks = input()

    # 현재 막대개수를 저장하고 쇠막대기 조각을 저장할 변수 선언
    count = 0
    piecs = 0
    
    # sticks에 저장된 문자열을 하나씩 꺼내와 반복
    for i in range(len(sticks)):
        if sticks[i] == '(':
            count += 1
        else:
            count -= 1
            if sticks[i - 1] == '(':
                piecs += count
            else:
                piecs += 1

    print(f'#{test_case} {piecs}')