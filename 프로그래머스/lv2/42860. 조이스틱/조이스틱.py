def solution(name):
    answer = 0
    min_move = len(name) - 1

    for idx, char in enumerate(name):

        answer += min(ord(char) - ord('A'), (ord('Z') + 1) - ord(char))

        next_value = idx + 1
        while next_value < len(name) and name[next_value] == 'A':
            next_value += 1

        min_move = min(min_move, (2 * idx + len(name) - next_value), idx + 2 * (len(name) - next_value))

    answer += min_move
    return answer