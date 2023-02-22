def solution(nums):
    answer = len(nums) // 2
    nums_set = len(set(nums))
    return nums_set if answer > nums_set else answer