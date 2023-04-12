def solution(N, number):
    dp = []
    for i in range(1, 9):
        dp.append(set([int(str(N)*i)]))

    for i in range(8):
        for j in range(i):
            for x in dp[j]:
                for y in dp[i-j-1]:
                    dp[i].add(x+y)
                    dp[i].add(x-y)
                    dp[i].add(x*y)
                    if y != 0:
                        dp[i].add(x//y)

        if number in dp[i]:
            return i + 1
    return -1