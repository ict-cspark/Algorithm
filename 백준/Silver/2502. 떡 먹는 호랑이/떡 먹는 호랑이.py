import sys
input = sys.stdin.readline

D, K = map(int, input().split())

for i in range(1, 100000):
    for j in range(i, 100000):
        cake = [0] * (D + 1)
        cake[1] = i
        cake[2] = j
        
        for k in range(3, D + 1):
            cake[k] = cake[k - 2] + cake[k -1]
            
        if cake[D] == K:
            print(cake[1])
            print(cake[2])
            exit()