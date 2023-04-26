def test(num, cnt):
    global result
    if num > 10:
        result += 1
        return

    for i in range(1, 6):
        if len(solve) < 2 or solve[-2] != solve[-1] or solve[-1] != i:
            solve.append(i)
            if answer[num] == i:
                test(num + 1, cnt + 1)
            else:
                if num - cnt > 5:
                    solve.pop()
                    continue
                test(num + 1, cnt)
            solve.pop()


answer = [0] + list(map(int, input().split()))
solve = []
result = 0
test(1, 0)
print(result)