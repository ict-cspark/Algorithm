def solution(binomial):
    answer = 0
    myList = list(map(str, binomial.split()))
    a = int(myList[0])
    b = int(myList[2])
    op = myList[1]
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    elif op == '*':
        answer = a * b
        
    return answer