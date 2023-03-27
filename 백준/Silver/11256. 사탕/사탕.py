T = int(input())

for _ in range(T):
    J, N = map(int, input().split())
    boxes = []
    for _ in range(N):
        R, C = map(int, input().split())
        boxes.append(R * C)

    boxes.sort(reverse=True)

    result = 0
    temp = 0
    for box in boxes:
        temp += box
        result += 1
        if temp >= J:
            break

    print(result)
