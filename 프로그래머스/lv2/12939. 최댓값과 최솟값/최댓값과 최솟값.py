def solution(s):
    s_new = list(map(int,s.split(" ")))
    answer = str(min(s_new)) + " " + str(max(s_new))
    return answer