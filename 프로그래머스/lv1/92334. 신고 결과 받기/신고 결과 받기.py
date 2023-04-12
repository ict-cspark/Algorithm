def solution(id_list, report, k):
    answer = []
    report = list(set(report))

    report_new = []
    for i in report:
        a,b = list(map(str,i.split(' ')))
        report_new += [[a, b]]

    report_user = []
    for i in report_new:
        report_user += [i[1]]

    report_ban = []
    for i in id_list:
        if report_user.count(i) >= k:
            report_ban += [i]

    report_notify = []
    for i in report_new:
        if i[1] in report_ban:
            report_notify += [i[0]]

    for i in id_list:
        answer += [report_notify.count(i)]
    
    return answer