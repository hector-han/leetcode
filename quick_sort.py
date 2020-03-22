

from typing import List


def partition(nums: List[int], start, end):
    """
    [start, end)
    """
    if start >= end - 1:
        return
    stash = nums[start]
    i, j = start, end - 1
    while i < j:
        while i < j and nums[j] >= stash:
            j -= 1
        nums[i] = nums[j]

        while i < j and nums[i] <= stash:
            i += 1
        nums[j] = nums[i]

    nums[i] = stash
    partition(nums, start, i)
    partition(nums, i+1, end)


def quick_sort(nums: List[int]):
    partition(nums, 0, len(nums))


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 100) for _ in range(10)]
    print(nums)
    quick_sort(nums)
    print(nums)
