def solution(numbers):
    numbers = list(map(str,numbers))
    final = sorted(numbers, key = lambda x : x*3 ,reverse=True)
    answer = ''.join(final)
    if answer[0] == '0':
        answer = '0'
    return answer