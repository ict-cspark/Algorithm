import sys
input = sys.stdin.readline

reverse = {1: 3, 2: 4, 3: 1, 4: 2}

N = int(input())
standard = list(map(int, input().split()))
T = int(input())
shapes = []
for _ in range(T):
    shape = list(map(int, input().split()))
    shapes.append(shape)

result = []
for shape in shapes:
    reverse_shape = []
    for s in shape:
        reverse_shape.append(reverse[s])
    reverse_shape = reverse_shape[::-1]

    if standard == shape or standard == reverse_shape:
        result.append(shape)
        continue

    for i in range(1, N):
        shape_trans = shape[i:] + shape[:i]
        reverse_shape_trans = reverse_shape[i:] + reverse_shape[:i]

        if standard == shape_trans or standard == reverse_shape_trans:
            result.append(shape)
            break

print(len(result))
for r in result:
    print(*r)