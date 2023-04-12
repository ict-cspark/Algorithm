def solution(n):
    fibo = [0,1]
    for i in range(2,n+1):
        result = fibo[i-1] + fibo[i-2]
        fibo.append(result)
    answer = fibo[n]%1234567
    return answer