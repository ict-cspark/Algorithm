def multi(arr):
    result = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            result.append(arr[i] * arr[j])
    return result

def numcheck(lst):
    lst.sort(reverse=True)
    for num in lst:
        num = str(num)
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                break
        else:
            return num
    return -1


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))

    numset = multi(num)
    result = numcheck(numset)
    # 결과값 출력
    print(f'#{test_case} {result}')