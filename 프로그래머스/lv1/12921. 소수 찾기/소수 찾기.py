import math
def solution(n):
    answer = 0
    for i in range(2,n+1):
        ans = 1
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                ans = ans+1
                if ans == 2:
                    break
        if ans == 1:
            answer = answer +1
    return answer