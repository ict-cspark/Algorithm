T = int(input())

for t in range(1,T+1):
    N = int(input())
    num = input()

    result = 0
    result_lst = []
    for i in num:
        if i == '1':
            result += 1
        else:
            result_lst.append(result)
            result = 0

    result_lst.append(result)
    result = max(result_lst)
    
    print(f'#{t} {result}')