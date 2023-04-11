
N = int(input())
result = N

for i in range(N):
    word = input()

    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                result -= 1
                break

print(result) 