import re

def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    option = {"":1, '*':2, '#':-1}
    
    p = re.compile('([0-9]+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    
    # 	[('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]
    for i in range(3):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2 
            
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    
    answer = sum(dart)
    return answer