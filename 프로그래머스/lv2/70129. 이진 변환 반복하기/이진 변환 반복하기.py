def solution(s):
    
    zero = 0
    cnt = 0
    while s != "1":
        temp = 0
        for a in s:
            if a == "1":
                temp += 1
            else:
                zero += 1
        
        trans = ""
        while temp > 0:
            if temp % 2:
                temp = temp // 2
                trans += "1"
            else:
                temp = temp // 2
                trans += "0"
        
        s = trans[::-1]
        cnt += 1
    
    answer = [cnt, zero]
    return answer