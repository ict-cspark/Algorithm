h, m = map(int, input().split(' '))

alarm_revise = ((h*60)+m) - 45

hh = alarm_revise//60
mm = alarm_revise%60

if hh == -1:
    hh = 23

print(hh,mm)