def solution(age):
    answer = ''
    for a in str(age):
        answer += chr(97 + int(a))
    return answer