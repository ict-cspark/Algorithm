from itertools import combinations

def solution(number):
    students = list(combinations(number, 3))

    answer = 0
    for student in students:
        if sum(student) == 0:
            answer += 1
    return answer