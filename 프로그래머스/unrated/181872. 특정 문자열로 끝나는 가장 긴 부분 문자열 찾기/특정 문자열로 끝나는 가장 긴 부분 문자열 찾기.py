def solution(myString, pat):
    for i in range(len(myString) - 1, len(pat) - 2, -1):
        if myString[i] == pat[-1]:
            for j in range(len(pat)):
                if myString[i-j] != pat[-(j+1)]:
                    break
            else:
                answer = myString[:i+1]
                break
                                
    return answer