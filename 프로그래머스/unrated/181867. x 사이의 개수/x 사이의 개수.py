def solution(myString):
    answer = []
    myList = list(map(str, myString.split('x')))
    for word in myList:
        answer.append(len(word))
    return answer