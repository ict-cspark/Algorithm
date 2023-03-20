N = int(input())
start = 1
end = N

while True:
    mid = (start + end) // 2
    if mid ** 2 == N:
        print(mid)
        break
    elif mid ** 2 > N:
        end = mid - 1
    elif mid ** 2 < N:
        start = mid + 1