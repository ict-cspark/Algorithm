def solution(myString):
    answer = []
    myList = list(map(str, myString.split('x')))
    myList.sort()
    for word in myList:
        if word != "":
            answer.append(word)
    
    return answer