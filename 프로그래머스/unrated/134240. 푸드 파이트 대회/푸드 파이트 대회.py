def solution(food):
    place = ''
    for i in range(1, len(food)):
        place += str(i) * (food[i] // 2)
    
    answer = place + '0' + place[::-1]
    return answer