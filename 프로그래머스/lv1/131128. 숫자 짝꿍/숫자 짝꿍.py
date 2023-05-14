def solution(X, Y):
    x_dict = dict()
    y_dict = dict()
    for i in range(10):
        x_dict[str(i)] = 0
        y_dict[str(i)] = 0
        
    for x in X:
        x_dict[x] += 1
    for y in Y:
        y_dict[y] += 1
    
    answer = ""
    for j in range(9, -1, -1):
        cnt = min(x_dict[str(j)], y_dict[str(j)])
        answer += str(j) * cnt
    
    if answer == "":
        answer = "-1"
    elif answer[0] == "0":
        answer = "0"
        
    return answer