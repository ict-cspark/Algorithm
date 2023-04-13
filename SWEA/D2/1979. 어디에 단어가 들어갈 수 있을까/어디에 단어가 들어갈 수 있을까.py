def puzzle_check(puzzle):
    length = 0
    result = 0
    for r in range(N + 1):
        for c in range(N + 1):
            if puzzle[r][c] == 1:
                length += 1
            else:
                if length == K:
                    result += 1
                    length = 0
                else:
                    length = 0
    return result

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):

    N, K = map(int, input().split())

    puzzle = []
    for _ in range(N):
        words = input() + ' 0'
        puzzle += [list(map(int, words.split()))]
    puzzle += [[0] * (N + 1)]
    puzzle_c = list(map(list, zip(*puzzle)))

    result = puzzle_check(puzzle) + puzzle_check(puzzle_c)
    print(f'#{test_case} {result}')