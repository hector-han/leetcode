import re
import time

def gen_pattern(n):
    pattern = 'a?' * n
    string = 'a' * n
    return pattern + string, string


def quick_sort(nums, begin, end):
    if begin + 1 > end:
        return
    key = nums[begin]
    i, j = begin, end
    while i < j:
        while j > i and nums[j] > key:
            j -= 1
        if j == i:
            break
        nums[i] = nums[j]
        while i < j and nums[i] <= key:
            i += 1
        if j == i:
            break
        nums[j] = nums[i]
    nums[j] = key
    quick_sort(nums, begin, j - 1)
    quick_sort(nums, j + 1, end)


if __name__ == '__main__':
    nums = [92, 1, 34, 39, 21, 75, 35, 99, 33, 89]
    print(nums)
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
