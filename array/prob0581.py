"""
最短无序连续子数组
easy

给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度。

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0
        i = 0
        while i + 1 < length and nums[i] <= nums[i + 1]:
            i += 1
        if i == length - 1:
            return 0
        j = length - 1
        while nums[j - 1] <= nums[j]:
            j -= 1

        minimum = min(nums[i:j + 1])
        maximum = max(nums[i:j + 1])
        while i >= 0 and nums[i] > minimum:
            i -= 1
        while j < length and nums[j] < maximum:
            j += 1
        return j - i - 1
