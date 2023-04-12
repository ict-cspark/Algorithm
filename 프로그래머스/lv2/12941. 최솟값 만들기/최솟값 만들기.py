def solution(A,B):
    answer = 0
    a = sorted(A)
    b = sorted(B,reverse=True)
    for x,y in zip(a,b):
        answer += x * y
    return answer