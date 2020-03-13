"""
Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""
from typing import List


class Solution:
    def flip(self, nums, i, j):
        _sum = i + j
        while i < _sum / 2:
            j = _sum - i
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        j = length - 1
        max_idx = length - 1
        while j >= 0:
            if nums[j] < nums[max_idx]:
                break
            else:
                max_idx = j
            j -= 1

        if j >= 0:
            i = length - 1
            while nums[i] <= nums[j]:
                i -= 1
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp
            self.flip(nums, j + 1, length - 1)
            return
        else:
            self.flip(nums, 0, length - 1)
