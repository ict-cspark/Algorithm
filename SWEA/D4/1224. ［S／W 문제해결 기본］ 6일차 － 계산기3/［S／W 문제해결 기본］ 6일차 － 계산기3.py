T = 10

ICP = {'(': 3, '+': 1, '*': 2}
ISP = {'(': 0, '+': 1, '*': 2}

op = {
    '+': lambda x,y: x + y,
    '*': lambda x,y: x * y,
}

def convert(calc):
    stack = []
    result = ''
    for i in calc:
        if i.isdecimal():
            result += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack != [] and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack != [] and  ICP[i] <= ISP[stack[-1]]:
                result += stack.pop()
            stack.append(i)
    while stack != []:
        result += stack.pop()

    return result

def number(num):
    number = []
    for n in num:
        if n.isdecimal():
            number.append(int(n))
        elif n in op:
            n2 = number.pop()
            n1 = number.pop()
            number.append(op[n](n1, n2))
    return number[-1]

for test_case in range(1, T + 1):
    N = int(input())
    calc = input()

    new_calc = convert(calc)
    result = number(new_calc)

    print(f'#{test_case} {result}')