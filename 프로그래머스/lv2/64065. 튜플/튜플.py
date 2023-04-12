def solution(s):

    s = s[2:-2].split('},{')
    
    number = []
    for i in s:
        number.append(i.split(','))
    
    number.sort(key=len)
    answer = []
    for num in number:
        for n in num:
            if int(n) not in answer:
                answer.append(int(n))
                break

    return answer