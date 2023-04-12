def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    temp = ''
    for i in new_id:
        if i.isalnum() or i == '-' or i == '_' or i == '.':
            if i == '.':
                if i != temp:
                    answer += '.'
                    temp = '.'
                else:
                    pass
            else:
                answer += i
                temp = ''

    while answer[0] == '.' or answer[-1] == '.':
        if answer[0] == '.':
            answer = answer[1:]
            if answer != '':
                if answer[-1] == '.':
                    answer = answer[:-1]
            else:
                break
        if answer[-1] == '.':
            answer = answer[:-1]
            if answer == '':
                break

    if answer == '':
        answer = 'a'
    else:
        pass

    if len(answer) >=16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
        else:
            pass
    else:
        pass

    if len(answer) <= 2:
        answer = answer.ljust(3,answer[-1])
    else:
        pass

    return answer