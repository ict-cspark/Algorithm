baby = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    answer = 0
    
    for i in range(len(babbling)):
        word = babbling[i]
        
        for j in baby:
            if j in word:
                word = word.replace(j, "0")
                
        if len(word) == word.count("0"):
            answer += 1
    return answer