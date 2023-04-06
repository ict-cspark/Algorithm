def solution(A, B):
    for i in range(len(A)):
        if A == B:
            answer = i
            break
        else:
            A = A[-1] + A[:-1]
    else:
        answer = -1

    return answer