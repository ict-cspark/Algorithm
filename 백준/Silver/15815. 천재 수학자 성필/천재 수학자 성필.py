import sys
input = sys.stdin.readline

mod = input()

op = ['+', '-', '*', '/']
stack = []
for m in mod:
    if m in op:
        b = int(stack.pop())
        a = int(stack.pop())

        if m == '+':
            answer = a + b
            stack.append(answer)
        elif m == '-':
            answer = a - b
            stack.append(answer)
        elif m == '*':
            answer = a * b
            stack.append(answer)
        else:
            answer = a // b
            stack.append(answer)
    else:
        stack.append(m)

print(stack[0])