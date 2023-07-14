N = input()

odd = N.count("1") // 2
even = N.count("0") // 2

N = list(N)
for _ in range(odd):
    idx = N.index("1")
    N.pop(idx)

N = N[::-1]
for _ in range(even):
    idx = N.index("0")
    N.pop(idx)

N = N[::-1]

result = "".join(N)
print(result)
