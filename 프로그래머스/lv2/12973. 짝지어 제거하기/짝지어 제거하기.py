def solution(s):
    
    stack = []
    for a in s:
        stack.append(a)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            
    if stack:
        answer = 0
    else:
        answer = 1
            
    return answer