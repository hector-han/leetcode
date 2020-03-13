"""
[LeetCode] Maximum Size Subarray Sum Equals k 最大子数组之和为k medium

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?

这个和滑动窗口没啥关系，累计和解法
"""

from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = 0
        sum = 0
        m = {}
        for i, num in enumerate(nums):
            sum += num
            if sum == k:
                ans = i+1
            elif (sum - k) in m:
                ans = max(i - m[sum-k], ans)
            if sum not in m:
                m[sum] = i
        return ans



