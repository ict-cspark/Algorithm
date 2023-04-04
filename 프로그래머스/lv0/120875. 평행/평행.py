def solution(dots):
    a = dots[:]
    b = [a.pop(0)]
    
    answer = 0
    for i in range(3):
        b.append(a.pop(0))
        
        ax = a[1][0] - a[0][0]
        ay = a[1][1] - a[0][1]
        bx = b[1][0] - b[0][0]
        by = b[1][1] - b[0][1]

        if (ay / ax) == (by / bx):
            answer = 1
            break
        
        a.append(b.pop())
        
    return answer