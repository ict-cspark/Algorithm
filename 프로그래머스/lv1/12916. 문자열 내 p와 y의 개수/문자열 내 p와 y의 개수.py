def solution(s):
    p = 0
    y = 0
    if len(s) <= 50:
        for i in range(len(s)):
            if s[i] == 'P' or s[i] == 'p':
                p = p+1
            elif s[i] == 'Y' or s[i] == 'y':
                y = y+1
        if p == y:
            return True
        else:
            return False
    return True