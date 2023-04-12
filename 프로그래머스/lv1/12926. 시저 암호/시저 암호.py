def solution(s, n):
    ans = ''
    res = 0
    result = 0
    
    for i in range(len(s)):
        if ord(s[i]) != 32:
            res = ord(s[i])
            if 97<= res <=122:
                result = res + int(n)
                if result > 122:
                    result = result - 26
            elif 65<= res <=90:
                result = res + int(n)
                if result >90:
                    result = result - 26
        else:
            result = ord(s[i])

        ans = ans + chr(result)
    return ans