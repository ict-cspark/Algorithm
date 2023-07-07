N = int(input())

if N == 0:
    print(0)
    exit()

flag = 0
if N < 0:
    flag = 1
    N *= -1

answer = []
while N > 0:
    R = N % 3
    if R == 2:
        R = -1
        answer.append("T")
    else:
        answer.append(str(R))
    N -= R
    N = N // 3


if flag == 1:
    for i in range(len(answer)):
        if answer[i] == "1":
            answer[i] = "T"
        elif answer[i] == "T":
            answer[i] = "1"

result = "".join(answer[::-1])
print(result)