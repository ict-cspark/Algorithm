def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        number = int(num[s : s + l])
        if number > k:
            answer.append(number)
    return answer