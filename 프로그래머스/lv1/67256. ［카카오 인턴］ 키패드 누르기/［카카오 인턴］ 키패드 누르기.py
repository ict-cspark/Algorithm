def solution(numbers, hand):
    answer = ''
    L = [3,0]
    R = [3,2]
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    for i in numbers:
        for j in range(4):
            if i == keypad[j][0]:
                answer += 'L'
                L = [j,0]
            elif i == keypad[j][2]:
                answer += 'R'
                R = [j,2]
            elif i == keypad[j][1]:
                C = [j,1]
                if hand == 'right':
                    if abs(C[0]-R[0])+abs(C[1]-R[1]) <= abs(C[0]-L[0])+abs(C[1]-L[1]):
                        answer += 'R'
                        R = [j,1]
                    else:
                        answer += 'L'
                        L = [j,1]
                elif hand == 'left':
                    if abs(C[0]-L[0])+abs(C[1]-L[1]) <= abs(C[0]-R[0])+abs(C[1]-R[1]):
                        answer += 'L'
                        L = [j, 1]
                    else:
                        answer += 'R'
                        R = [j, 1]
    return answer