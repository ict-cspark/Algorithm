def solution(s):
    answer = 0

    alph = s[0]
    idx = 1
    a = 1
    b = 0
    while len(s) > idx:
        if alph == s[idx]:
            a += 1
        else:
            b += 1
        idx += 1

        if a == b:
            answer += 1
            if len(s) > idx:
                alph = s[idx]
                s = s[idx:]
                idx = 1
                a = 1
                b = 0
            else:
                break

    if a != b:
        answer += 1

    return answer