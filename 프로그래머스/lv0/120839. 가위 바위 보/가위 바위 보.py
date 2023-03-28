win = {"2": "0", "5": "2", "0": "5"}

def solution(rsp):
    answer = ''
    for r in str(rsp):
        answer += win[r]
    return answer