def findDisappearedNumbers(nums):
    len_nums = len(nums)
    diff = list(set(range(1, len_nums+1)) - set(nums))

    return diff