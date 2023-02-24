S = input()
result = ''
for i in range(97,123):
    if chr(i) in S:
        result = result + str(S.index(chr(i))) + ' '
    else:
        result = result + '-1' + ' '

print(result[:-1])