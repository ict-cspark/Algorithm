# 테스트 케이스 입력
T = int(input())

for t in range(1, T + 1):
    # test 번호와 테스트 길이와 테스트 케이스를 입력받기
    test, case = map(str, input().split())
    words = list(map(str,input().split()))

    # 외계행성의 숫자체계가 담긴 딕셔너리 생성
    planet = {"ZRO" : 0, "ONE" : 0, "TWO" : 0, "THR" : 0, "FOR" : 0, "FIV" : 0, "SIX" : 0, "SVN" : 0, "EGT" : 0, "NIN" : 0}
    
    # words 리스트를 순차적으로 탐색하면서 planet에 키 값과 일치하면 1을 추가
    for i in words:
        planet[i] += 1

    # 0~9 까지 반복문을 돌면서 planet 딕셔너리에 저장되어있는 개수만큼 곱해서 result에 순서대로 저장
    # planet.items()를 이용하여 key값과 value 값을 리스트에 저장하여 순차적으로 호출
    result = ""
    planet_lst = list(planet.items())

    for j in range(10):
        result += (planet_lst[j][0] + " ") * planet_lst[j][1]

    # 결과값 출력
    print(test)
    print(result)