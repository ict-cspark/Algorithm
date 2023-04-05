def solution(id_pw, db):
    
    for data in db:
        if id_pw == data:
            answer = "login"
            break
    else:
        for data in db:
            if id_pw[0] == data[0]:
                answer = "wrong pw"
                break
        else:
            answer = "fail"
            
    return answer