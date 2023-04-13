delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(atom)):
        atom[i][0] = atom[i][0] * 2
        atom[i][1] = atom[i][1] * 2

    result = 0
    for _ in range(4002):
        dd = set()
        for kk in range(len(atom)):
            dd.add(atom[kk][2])
        if len(dd) == 1:
            break
        for k in range(len(atom) - 1, -1, -1):
            if abs(atom[k][0]) > 2000 or abs(atom[k][1]) > 2000:
                atom.pop(k)
        for d in range(len(atom)):
            atom[d][0] += delta[atom[d][2]][1]
            atom[d][1] += delta[atom[d][2]][0]

        delete = set()
        visit = set()
        for n in range(len(atom)):
            nc = atom[n][0]
            nr = atom[n][1]
            if (nc, nr) in visit:
                delete.add((nc, nr))
            visit.add((nc, nr))

        for j in range(len(atom) - 1, -1, -1):
            if (atom[j][0], atom[j][1]) in delete:
                result += atom[j][3]
                atom.pop(j)

        if len(atom) < 2:
            break
    print(f'#{test_case} {result}')