def solution(left, right):
    answer = 0
    exp = 0
    for i in range(left,right+1):
        answer = answer + i
        for j in range(1,i+1):
            if i == j*j:
                exp = exp + i
                break
    answer = answer - (2*exp)
    return answer