def palindrome(words):
    for i in range(100, 0, -1):
        for c in range(100):
            for r in range(100 - (i - 1)):
                if words[c][r:r+i] == words[c][r:r+i][::-1]:
                    return i


# 테스트 케이스 입력 받기

T = 10

for t in range(1, T + 1):
    N = int(input())

    words_row = []
    words_col = []

    for n in range(100):
        words_row += [list(map(str, input()))]
    words_col = list(map(list,zip(*words_row)))

    row_result = palindrome(words_row)
    col_result = palindrome(words_col)

    if row_result >= col_result:
        print(f'#{N} {row_result}')
    else:
        print(f'#{N} {col_result}')