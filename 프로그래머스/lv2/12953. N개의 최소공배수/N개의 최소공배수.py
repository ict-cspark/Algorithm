def max_num(a,b):
    c = max(a,b)
    for i in range(1,c+1):
        if a%i == 0 and b%i == 0:
            answer = i
    return answer

def solution(arr):
    result = []
    LCM = arr[0]
    for i in range(len(arr)-1):
        GCD = max_num(int(LCM),arr[i+1])
        LCM= LCM*arr[i+1]/GCD
        result.append(LCM)
    answer = int(max(result))
    return answer