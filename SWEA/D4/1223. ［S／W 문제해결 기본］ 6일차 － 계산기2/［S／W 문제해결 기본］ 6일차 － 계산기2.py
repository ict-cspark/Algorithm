T = 10

for test_case in range(1, T + 1):
    N = int(input())
    num = input()

    pri = {'+': 1,'*': 2} # 연산자 우선순위

    st_num = []
    st_oper = []
    for i in range(N):
        if num[i].isdecimal():
            st_num.append(int(num[i]))

        elif st_oper != []:
            while st_oper != [] and len(st_num) >= 2 and pri[num[i]] <= pri[st_oper[-1]]:
                p2 = st_num.pop()
                p1 = st_num.pop()
                if pri[st_oper[-1]] == 2:
                    st_num.append(p1 * p2)
                    st_oper.pop()
                else:
                    st_num.append(p1 + p2)
                    st_oper.pop()
            st_oper.append(num[i])
        else:
            st_oper.append(num[i])

    while st_oper:
        p2 = st_num.pop()
        p1 = st_num.pop()
        if pri[st_oper[-1]] == 2:
            st_num.append(p1 * p2)
            st_oper.pop()
        else:
            st_num.append(p1 + p2)
            st_oper.pop()

    print(f'#{test_case} {st_num[0]}')