def solution(brown, yellow):
    result = (brown - 4) // 2

    for i in range(1, result + 1):
        if i > yellow:
            break
        if yellow % i == 0:
            print(i)
            j = result - i
            if (i * j) == yellow:
                break
    if i > j:
        answer = [i + 2, j + 2]
    else:
        answer = [j + 2, i + 2]
    return answer