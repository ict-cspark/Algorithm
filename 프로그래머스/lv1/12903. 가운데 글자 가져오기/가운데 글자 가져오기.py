def solution(s):
    l = len(s)
    if l%2==0:
        answer = s[int(l/2)-1] + s[int(l/2)]
    else:
        answer = s[int(l/2)]
    return answer