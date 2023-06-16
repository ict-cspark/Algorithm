def solution(s):
    answer = 0
    N = len(s)
    for i in range(N):
        rotate = s[i:] + s[:i]
        queue = []
        for r in rotate:
            if r == "[" or r == "(" or r == "{":
                queue.append(r)
            else:
                if not queue:
                    queue.append(-1)
                    break
                    
                if r == "]":
                    if queue and queue[-1] == "[":
                        queue.pop()

                elif r == ")":
                    if queue and queue[-1] == "(":
                        queue.pop()
                        
                elif r == "}":
                    if queue and queue[-1] == "{":
                        queue.pop()
        
        if not queue:
            answer += 1
    
    return answer