def solution(record):

    newRecord = []
    idStatus = dict()
    for r in record:
        nr = list(map(str, r.split()))
        newRecord.append(nr)
        if nr[0] != 'Leave':
            idStatus[nr[1]] = nr[2]

    answer = []
    message = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for ans in newRecord:
        if ans[0] != 'Change':
            result = idStatus[ans[1]] + message[ans[0]]
            answer.append(result)
    
    return answer