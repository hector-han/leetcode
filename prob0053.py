"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_end = nums[0]
        for num in nums[1:]:
            max_end = max(max_end + num, num)
            max_so_far = max(max_so_far, max_end)
        return max_so_far

if __name__ == '__main__':
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sol.maxSubArray(nums))
