atom = {"H": 1, "C": 12, "O": 16}

words = input()
stack = []

for word in words:
    if word == "(":
        stack.append(word)
    elif word == ")":
        temp = 0
        while True:
            answer = stack.pop()
            if answer == "(":
                stack.append(temp)
                break
            else:
                temp += answer

    else:
        if word.isdecimal():
            stack.append(stack.pop() * int(word))
        else:
            stack.append(atom[word])

print(sum(stack))