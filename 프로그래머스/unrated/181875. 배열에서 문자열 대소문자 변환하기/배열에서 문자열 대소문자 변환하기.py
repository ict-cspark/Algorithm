def solution(strArr):
    for i in range(len(strArr)):
        word = strArr[i]
        if i % 2:
            strArr[i] = word.upper()
        else:
            strArr[i] = word.lower()
    return strArr