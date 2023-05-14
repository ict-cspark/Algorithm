def solution(number, limit, power):
    numbers = [0] * (number + 1)
    for n in range(1, number + 1):
        cnt = 0
        for m in range(1, int(n**(1/2) + 1)):
            if n % m == 0:
                cnt += 1
                if m ** 2 != n:
                    cnt += 1
        numbers[n] = cnt
    
    answer = 0
    for num in numbers:
        if num <= limit:
            answer += num
        else:
            answer += power
            
    return answer