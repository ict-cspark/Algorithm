def solution(polynomial):
    poly_list = list(map(str, polynomial.split()))

    a = 0
    b = 0
    for poly in poly_list:
        if poly != '+':
            if poly.find('x') != -1:
                if len(poly) > 1:
                    a += int(poly[:-1])
                else:
                    a += 1
            else:
                b += int(poly)
                
    answer = ""
    if a > 0:
        if a == 1:
            answer += 'x'
        else:
            answer += f'{a}x'
        
    if b > 0:
        if a > 0:
            answer += ' + '
        answer += str(b)
        
    return answer