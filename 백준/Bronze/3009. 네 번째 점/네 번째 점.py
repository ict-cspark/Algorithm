def my_only(a,b,c):
    if a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a

a,x = map(int,input().split())
b,y = map(int,input().split())
c,z = map(int,input().split())

print(my_only(a, b, c), my_only(x, y, z))