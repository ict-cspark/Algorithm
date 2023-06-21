import sys
input = sys.stdin.readline


def win(T):
    if T["1"] != T["2"]:
        if T["1"] > T["2"]:
            return "1"
        else:
            return "2"
    else:
        return "0"


def second(t):
    answer = ((int(t[:2]) * 60) + int(t[3:]))
    return answer


N = int(input())

team_score = {"1": 0, "2": 0}
team_time = {"1": 0, "2": 0}
time_flag = 0
for _ in range(N):
    winner = win(team_score)
    team, time = input().split()
    team_score[team] += 1
    if team_score["1"] == team_score["2"]:
        result = second(time)
        team_time[winner] += result - time_flag
    else:
        if winner == "0":
            winner_new = win(team_score)
            result = second(time)
            time_flag = result

winner = win(team_score)
if winner != "0":
    team_time[winner] += (60 * 48) - time_flag

for value in team_time.values():
    minute = value // 60
    second = value % 60
    result = str(minute).zfill(2) + ":" + str(second).zfill(2)
    print(result)