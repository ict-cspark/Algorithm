# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    # 다섯 줄의 단어를 입력 받고 2차원 행렬로 바꾸기
    words = []
    for _ in range(5):
        words += [list(map(str, input()))]

    result = ''
    for c in range(15):
        for r in range(5):
            if len(words[r]) > c:
                result += words[r][c]
            else:
                continue

    print(f'#{test_case} {result}')