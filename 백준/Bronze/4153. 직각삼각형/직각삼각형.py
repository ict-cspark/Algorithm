while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    max_num = max(a, b, c)**2

    sqrt_num = (a**2) + (b**2) + (c**2)

    if sqrt_num == max_num * 2:
        print('right')
    else:
        print('wrong')