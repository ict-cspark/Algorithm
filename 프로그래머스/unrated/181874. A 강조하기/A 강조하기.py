def solution(myString):
    myString = myString.lower()
    myList = list(myString)
    for i in range(len(myList)):
        if myList[i] == 'a':
            myList[i] = 'A'
    
    answer = ''.join(myList)
    return answer