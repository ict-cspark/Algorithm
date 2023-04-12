def solution(price, money, count):
    ans = 0
    for i in range(1,count+1):
        ans = ans + price*i
    answer = ans - money
    if answer < 0:
        answer = 0
    return answer