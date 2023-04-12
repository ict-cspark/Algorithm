def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    answer = []
    rank_count = 0
    zero_count = lottos.count(0)
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                rank_count = rank_count+1
                break
    max = 7 - (rank_count+zero_count)
    if max == 7:
        max = 6
    answer.append(max)
    min = 7 - rank_count
    if min == 7:
        min = 6
    answer.append(min)
    return answer