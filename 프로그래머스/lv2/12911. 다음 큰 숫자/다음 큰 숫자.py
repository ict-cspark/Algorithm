def solution(n):
    n_b = format(n,'b')
    count = n_b.count('1')
    n_max = n + 1
    while True:
        n_max_b = format(n_max,'b')
        count_max = n_max_b.count('1')
        if count == count_max:
            answer = n_max
            break
        else:
            n_max += 1
    return answer