def solution(nums):

    unique_types = len(set(nums))

    max_select = len(nums) // 2

    return min(unique_types, max_select)
