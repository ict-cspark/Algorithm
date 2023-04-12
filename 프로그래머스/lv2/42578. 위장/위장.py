def solution(clothes):

    clothes_hash = {}
    for name, sort in clothes:
        clothes_hash[sort] = clothes_hash.get(sort, 0) + 1
        
    answer = 1
    for sort in clothes_hash:
        answer *= (clothes_hash[sort] + 1)

    return answer - 1
