def dateToDay(date):
    year, month, day = map(int, date.split("."))
    result = (year * 12 * 28) + (month * 28) + day
    return result


def solution(today, terms, privacies):
    today = dateToDay(today)

    terms_dic = dict()
    for t in range(len(terms)):
        terms[t] = list(map(str, terms[t].split()))
        terms_dic[terms[t][0]] = int(terms[t][1]) * 28

    for p in range(len(privacies)):
        privacies[p] = list(map(str, privacies[p].split()))
        privacies[p] = dateToDay(privacies[p][0]) + terms_dic[privacies[p][1]] - 1

    answer = []
    for i in range(len(privacies)):
        if today > privacies[i]:
            answer.append(i + 1)

    return answer