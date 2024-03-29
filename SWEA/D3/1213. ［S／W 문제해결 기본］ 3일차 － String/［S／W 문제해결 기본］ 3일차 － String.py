T = 10

for t in range(1, T+1):
    N = int(input())
    special = input()
    words = input()

    # 문장을 탐색하면서 찾을 문자열의 첫글자를 찾아서
    # 해당 인덱스 위치를 저장할 빈 리스트를 만들고 인덱스 값을 저장
    sp_index = []
    for i in range(len(words)):
        if words[i] == special[0]:
            sp_index.append(i)

    # 저장된 인덱스 위치부터 단어 길이만큼 다시 검색해서 그 찾을 문자열이 맞으면 결과값에 1을 추가
    result = 0
    for j in sp_index:
        if words[j:j+len(special)] == special:
            result += 1

    # 결과값 출력
    print(f'#{t} {result}')