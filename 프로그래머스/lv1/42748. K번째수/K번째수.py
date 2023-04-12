def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        ans = array[a-1:b]
        ans.sort()
        answer.append(ans[c-1])
    return answer