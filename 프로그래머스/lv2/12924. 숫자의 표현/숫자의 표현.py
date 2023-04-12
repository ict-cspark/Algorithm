def solution(n):
    answer = 0
    sum = 0
    start = 1
    while start != n+1:
        for i in range(start,n+1):
            sum += i
            if sum == n:
                answer += 1
                start += 1
                sum = 0
                break
            elif sum > n:
                start += 1
                sum = 0
                break
    return answer