def queen(record, row, n):
    if row == n:
        return 1

    cnt = 0
    for col in range(n):
        if check(record, row, col):
            record[row] = col
            cnt += queen(record, row + 1, n)

    return cnt


def check(record, row, col):
    for r in range(row):
        if record[r] == col:
            return False
        if row - r == abs(col - record[r]):
            return False

    return True


def solution(n):
    record = [0] * n

    answer = queen(record, 0, n)
    return answer