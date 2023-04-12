def solution(numbers):
    answer = 0
    num = []
    for i in range(10):
        num.append(i)
    for i in range(len(numbers)):
        num.remove(numbers[i])

    answer = sum(num)
    return answer