def solution(n, arr1, arr2):
    answer = []
    arr = []
    result = []

    for i in range(n):
        arr.append(arr1[i]|arr2[i])
        result.append(format(pow(2,n)|arr[i],'b'))
        result[i] = result[i][1:]
        code = result[i].replace('1','#')
        code = code.replace('0',' ')
        answer.append(code)

    return answer