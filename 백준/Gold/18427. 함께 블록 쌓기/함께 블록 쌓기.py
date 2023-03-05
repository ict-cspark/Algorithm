import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
result = [0] * (H + 1)

for student in students:
    for h in range(H, 0, -1):
        for box in student:
            answer = h + box
            if answer <= H:
                result[answer] += result[h]

    for box in student:
        result[box] += 1

print(result[H] % 10007)