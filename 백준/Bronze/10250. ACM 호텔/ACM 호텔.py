T = int(input())

for i in range(T):
    H, W, N = map(int, input().split(' '))
    if N%H == 0:
        Y = N//H
        X = H
    else:
        Y = (N//H) + 1
        X = N%H
    
    YY = str(Y).rjust(2, '0')
    result = int(str(X) + YY)
    print(result)