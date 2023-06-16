def solution(elements):
    N = len(elements)
    elements_new = elements * 2
    
    result = set()
    for i in range(1, N + 1):
        for j in range(N):
            part = elements_new[j:j+i]
            result.add(sum(part))
            
    answer = len(result)
    return answer