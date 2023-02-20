import sys
input = sys.stdin.readline

while True:
    words = input().rstrip()

    if words == '.':
        break
    else:
        bracket = []
        for word in words:
            if word == '(' or word == '[':
                bracket.append(word)
            elif word == ')':
                if bracket and bracket[-1] == '(':
                    bracket.pop()
                else:
                    print('no')
                    break
            elif word == ']':
                if bracket and bracket[-1] == '[':
                    bracket.pop()
                else:
                    print('no')
                    break
        else:
            if not bracket:
                print('yes')
            else:
                print('no')