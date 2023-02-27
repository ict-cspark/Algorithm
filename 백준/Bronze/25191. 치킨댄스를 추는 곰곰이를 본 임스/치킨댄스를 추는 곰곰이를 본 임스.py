chicken = int(input())
coke, beer = map(int, input().split())

possible = (coke//2) + beer

if chicken > possible:
    print(possible)
else:
    print(chicken)