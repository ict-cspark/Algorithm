def solution(n, m):
    answer = []
    a = 0
    b = 0
    for i in range(1,max(n,m)):
        if n%i == 0 and m%i == 0:
            a = i
    b = n*m / a
    answer = [a,b]
    return answer