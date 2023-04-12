def solution(s):
    ans = s.split(" ")
    result = ""
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if j%2 == 0:
                result += ans[i][j].upper()
            else:
                result += ans[i][j].lower()
        result += " "
    return result[:-1]