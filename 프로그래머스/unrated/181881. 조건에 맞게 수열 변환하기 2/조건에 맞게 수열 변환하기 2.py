def solution(arr):
    answer = 0
    temp = arr[:]
    while True:
        for i in range(len(temp)):
            num = temp[i]
            if num >= 50 and num % 2 == 0:
                temp[i] = num // 2
            elif num < 50 and num % 2:
                temp[i] = (num * 2) + 1
            
        if arr == temp:
            break
        else:
            answer += 1
            arr = temp[:]

    return answer