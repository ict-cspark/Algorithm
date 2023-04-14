H, M = map(int, input().split())
time = int(input())

M += time

hour = (H + M//60) % 24
minute = M % 60

print(hour, minute)