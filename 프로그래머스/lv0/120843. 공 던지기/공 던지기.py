def solution(numbers, k):
    answer = ((k * 2) - 2) % len(numbers)
    return numbers[answer]