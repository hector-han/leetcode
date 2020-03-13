"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""

from typing import List


class Solution:
    """
    Boyer-Moore 投票算法
    """
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        ans = nums[0]
        for i in range(0, len(nums)):
            if nums[i] == ans:
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                ans = nums[i+1]
        return ans