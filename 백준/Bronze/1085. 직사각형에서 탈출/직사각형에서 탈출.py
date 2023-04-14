x, y, w, h = map(int, input().split())

xw = 0
yh = 0

if w - x <= x:
    xw = w - x
else:
    xw = x

if h - y <= y:
    yh = h - y
else:
    yh = y

result = min(xw, yh)
print(result) 