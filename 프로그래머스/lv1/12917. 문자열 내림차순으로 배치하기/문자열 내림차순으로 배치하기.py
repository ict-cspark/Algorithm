def solution(s):
    ans = []
    answer = ''
    for i in range(len(s)):
        ans.append(ord(s[i]))
    ans.sort(reverse=True)
    for i in range(len(s)):
        answer = answer + chr(ans[i])
    return answer