T = 10

for t in range(1, T+1):
    N = int(input())
    # 100x100 2차원 배열 입력받아 data 2차원 배열 생성
    data = []
    for n in range(100):
        data += [list(map(int, input().split()))]

    # 좌, 우, 위로 구성된 델타 배열 생성
    dr = [0, 0, -1]
    dc = [-1, 1, 0]
    # 마지막줄에서 2를 찾아 역으로 올라가면서 찾기
    nc = 0
    for i in range(100):
        if data[99][i] == 2:
            nc = i
            break
    nr = 99
    while nr != 0:
        for d in range(3):
            new_nr = nr + dr[d]
            new_nc = nc + dc[d]
            while 0 <= new_nr < 100 and 0 <= new_nc < 100 and 0 < data[new_nr][new_nc] < 2:
                data[new_nr][new_nc] = 2
                nr += dr[d]
                nc += dc[d]
    print(f'#{t} {nc}')