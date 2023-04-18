import sys
input = sys.stdin.readline

N = int(input())

stack = []
result = []
start = 1
flag = True

for i in range(N):
    num = int(input())
    while start <= num:
        stack.append(start)
        result.append("+")
        start += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = False
        break

if flag:
    for r in result:
        print(r)
else:
    print("NO")