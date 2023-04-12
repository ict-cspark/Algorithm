alph = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def solution(n, t, m, p):
    num = ['0'] * (t * m)
    for i in range(1, len(num)):
        change = ''
        ans = i
        while ans > 0:
            temp = ans % n
            if 10 <= temp <= 15:
                temp = alph[temp]
            ans = ans // n
            change = str(temp) + change
        num[i] = change

    answer = ''.join(num)
    result = ''
    for j in range(t):
        result += answer[(j * m) + (p - 1)]
        
    return result