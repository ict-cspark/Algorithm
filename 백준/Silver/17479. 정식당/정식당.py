import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

mainMenu = dict()
specialMenu = dict()
serviceMenu = []

for _ in range(A):
    menu, price = map(str, input().split())
    mainMenu[menu] = int(price)

for _ in range(B):
    menu, price = map(str, input().split())
    specialMenu[menu] = int(price)

for _ in range(C):
    menu = input().strip()
    serviceMenu.append(menu)

mainTotal = 0
specialTotal = 0
serviceCnt = 0
N = int(input())
for _ in range(N):
    menu = input().strip()
    if menu in mainMenu:
        mainTotal += mainMenu[menu]
    elif menu in specialMenu:
        specialTotal += specialMenu[menu]
    else:
        serviceCnt += 1

result = "Okay"
if mainTotal < 20000 and specialTotal > 0:
    result = 'No'
elif mainTotal + specialTotal < 50000 and serviceCnt > 0:
    result = 'No'
elif serviceCnt > 1:
    result = 'No'

print(result)