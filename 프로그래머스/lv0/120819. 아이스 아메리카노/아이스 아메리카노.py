def solution(money):
    cups = money // 5500
    change = money % 5500
    
    answer = [cups, change]
    return answer