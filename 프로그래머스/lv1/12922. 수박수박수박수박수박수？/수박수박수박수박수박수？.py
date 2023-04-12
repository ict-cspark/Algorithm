def solution(n):
    ans = ''
    n = int(n)
    if n <=10000:
        for i in range(1,n+1):
            if i%2 != 0:
                ans = ans + '수'
            else:
                ans = ans + '박'
        return ans