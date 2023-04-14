num = []
for i in range(9):
    num.append(int(input()))

max_num = max(num)
max_index = num.index(max_num)

print(max_num)
print(max_index+1)