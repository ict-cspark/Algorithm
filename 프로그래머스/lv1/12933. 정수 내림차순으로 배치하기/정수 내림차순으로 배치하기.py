def solution(n):
    answer = 0
    sol=[] 
    while True:
        sol += [n%10]
        if n < 10:
            break
        n = int(n/10)
    sol.sort(reverse=True)
    for i in sol:
        answer+=i
        answer*=10
    answer/=10
    return answer