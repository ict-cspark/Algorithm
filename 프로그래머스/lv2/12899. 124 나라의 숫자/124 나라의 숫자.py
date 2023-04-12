change = {1: '1', 2: '2', 0: '4'}  # 3진법과 대응하기 위한 change 딕셔너리 생성


def solution(n):
    answer = ''

    while n > 0:  # n이 0보다 클때까지 반복문 실행
        temp = n % 3  # n을 3으로 나눈 나머지를 temp에 저장
        if temp:  # temp가 0이 아니라면
            n = n // 3  # n을 3으로 나눈 몫을 n에 저장
        else:  # temp가 0일 경우
            n = (n // 3) - 1  # 자릿수를 맞추기 위해 n을 3을 나눈 몫에 1을 뺀값을 저장
        answer = change[temp] + answer  # answer에 chage[temp] + answer 값을 저장

    return answer  # answr 값을 반환