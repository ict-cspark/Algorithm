def solution(phone_number):
    lst = list(phone_number)
    a = lst[:-4]
    b = lst[-4:]
    c = '*' * len(a)
    d = ''.join(b)
    answer = c + d
    return answer