alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def solution(s, skip, index):
    
    alph_update = alph[:]
    for sk in skip:
        alph_update.remove(sk)
    
    answer = ''
    for sa in s:
        idx = (alph_update.index(sa) + index) % (26 - len(skip))
        answer += alph_update[idx]
        
    return answer