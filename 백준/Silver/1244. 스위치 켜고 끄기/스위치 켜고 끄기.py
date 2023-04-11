N = int(input())
switch = [0] + list(map(int, input().split()))
S = int(input())

student = [tuple(map(int, input().split())) for _ in range(S)]

for i in range(S):
    if student[i][0] == 1:       # 남자일 경우
        for b in range(0, N + 1, student[i][1]):
            switch[b] = not switch[b]
    else:                   # 여자일 경우
        girl = student[i][1]
        switch[girl] = not switch[girl]
        for g in range(1, N):
            sg = girl - g
            eg = girl + g
            if 0 < sg <= N and 0 < eg <= N and switch[sg] == switch[eg]:
                switch[sg] = not switch[sg]
                switch[eg] = not switch[eg]
            else:
                break

for s in range(len(switch)):
    if switch[s]:
        switch[s] = 1
    else:
        switch[s] = 0

switch.pop(0)

while switch:
    for _ in range(20):
        if switch:
            print(switch.pop(0), end=' ')
        else:
            break
    print()