def solution(lines):
    numbers = [0] * 201
    
    for line in lines:
        for i in range(line[0] + 101, line[1] + 101):
            numbers[i] += 1
    
    answer = 0
    for j in range(201):
        if numbers[j] > 1:
            answer += 1
    return answer