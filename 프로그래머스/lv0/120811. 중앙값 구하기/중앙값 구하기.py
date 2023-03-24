def solution(array):
    length = len(array)
    array.sort()
    answer = array[length // 2]
    return answer