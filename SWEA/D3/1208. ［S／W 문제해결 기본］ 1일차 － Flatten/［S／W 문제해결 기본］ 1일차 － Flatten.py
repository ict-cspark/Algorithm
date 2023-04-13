def my_sort(num):
    for i in range(100):
        for j in range(100):
            if num[i] < num[j]:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
    return num

T = 10

for i in range(1, T+1):
    dump = int(input())
    num = list(map(int, input().split()))
    new_num = my_sort(num)
    for j in range(dump):
        new_num[-1] -= 1
        new_num[0] += 1
        new_num = my_sort(new_num)

    print(f'#{i} {new_num[-1] - new_num[0]}')
